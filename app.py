import streamlit as st
import numpy as np
from pydub import AudioSegment
import os
from moviepy.editor import VideoFileClip
from difflib import SequenceMatcher
from vosk import Model as VoskModel, KaldiRecognizer
import wave
import json
from feedback import generate_phoneme_feedback  # Importing from separate file
from phoneme_analysis import analyze_phonemes  # Importing the phoneme analysis function

# Importing additional functionalities for tabs
from train_yourself import display_train_yourself
from send_report import send_report

# Paths to the Vosk model
vosk_model_path = "vosk-model-small-en-us-0.15"

# Load the Vosk model
if not os.path.exists(vosk_model_path):
    st.error("Please download the Vosk model from https://alphacephei.com/vosk/models and unpack as 'vosk-model-small-en-us-0.15' in the current folder.")
    exit(1)

vosk_model = VoskModel(vosk_model_path)

# Function to load HTML content
def load_html(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    
    # Load custom HTML and CSS for styling
st.markdown(load_html("Frontend/home.html"), unsafe_allow_html=True)


# # Custom HTML and CSS for styling and recording video
# st.markdown("""
#     <style>
#     .title {
#         font-size: 50px;
#         font-weight: bold;
#         text-align: center;
#     }
#     .subtitle {
#         font-size: 20px;
#         text-align: center;
#     }
#     .uploader {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }
#     .button {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }
#     .results {
#         margin-top: 20px;
#         padding: 10px;
#         background-color: #f9f9f9;
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# Navigation bar using tabs
tab = st.sidebar.radio("Navigation", ["Home", "Train Yourself", "Send Report"])

if tab == "Home":
    # Title and description
    st.markdown('<div class="title">Speech Analysis for Children</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">This app analyzes speech from children trying to pronounce words. It identifies issues with phonemes and provides suggestions for improvement. Upload a video of the child speaking and provide the expected phrase.</div>', unsafe_allow_html=True)

    # Video upload
    st.markdown('<div class="uploader">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "mov", "avi"])
    st.markdown('</div>', unsafe_allow_html=True)

    expected_text = st.text_input("Enter the expected word or phrase:", "")

    def extract_audio_from_video(video_file_path):
        video_clip = VideoFileClip(video_file_path)
        audio_path = "temp_audio.wav"
        video_clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
        video_clip.close()
        return audio_path

    def transcribe_audio_vosk(audio_file_path):
        wf = wave.open(audio_file_path, "rb")
        if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
            raise ValueError("Audio file must be WAV format mono PCM with a sample rate of 16000 Hz.")
        
        rec = KaldiRecognizer(vosk_model, wf.getframerate())
        transcription = []

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                result = rec.Result()
                transcription.append(result)
            else:
                rec.PartialResult()

        transcription.append(rec.FinalResult())
        text = ' '.join([eval(res)["text"] for res in transcription])
        wf.close()
        return text

    def analyze_transcription(transcription, expected_text):
        expected_words = expected_text.split()
        transcribed_words = transcription.split()
        analysis = []

        for expected, transcribed in zip(expected_words, transcribed_words):
            similarity = SequenceMatcher(None, expected, transcribed).ratio()
            analysis.append({
                "expected": expected,
                "transcribed": transcribed,
                "similarity": similarity
            })
        
        overall_similarity = SequenceMatcher(None, expected_text, transcription).ratio()
        return analysis, overall_similarity

    def generate_suggestions(analysis):
        suggestions = []
        for item in analysis:
            if item['similarity'] < 0.8:
                phoneme_feedback = generate_phoneme_feedback(item['expected'][0])
                suggestion = f"Improve the pronunciation of '{item['expected']}'. {phoneme_feedback}"
                suggestions.append(suggestion)
        return suggestions

    if uploaded_file is not None and expected_text and st.button('Analyze'):
        st.markdown('<div class="results">', unsafe_allow_html=True)
        
        # Save the uploaded video file
        with open("uploaded_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.video(uploaded_file)
        
        # Extract audio from the video
        audio_file_path = extract_audio_from_video("uploaded_video.mp4")
        
        # Ensure the audio is in the correct format
        audio = AudioSegment.from_wav(audio_file_path)
        audio = audio.set_channels(1).set_frame_rate(16000)
        audio.export("temp_audio_mono.wav", format="wav")

        # Transcribe the audio using Vosk
        transcription = transcribe_audio_vosk("temp_audio_mono.wav")
        
        st.write("**Expected Phrase:**")
        st.write(expected_text)
        
        st.write("**Transcription:**")
        st.write(transcription)
        st.audio("temp_audio_mono.wav")  # Provide control over the audio playback
        
        # Detailed Analysis using similarity matching
        analysis, overall_similarity = analyze_transcription(transcription, expected_text)
        st.write("### Detailed Analysis")
        for item in analysis:
            st.write(f"Expected: {item['expected']}, Transcribed: {item['transcribed']}, Similarity: {item['similarity']:.2f}")
            if item['similarity'] < 1.0:
                st.write(f"- Suggestion: Practice saying '{item['expected']}' more clearly.")
        
        st.write(f"**Overall Similarity Score:** {overall_similarity:.2f}")

        # Get the phoneme analysis
        phoneme_analysis = analyze_phonemes(transcription)
        st.write("### Phoneme-level Analysis")
        for result in phoneme_analysis:
            st.write(f"Phoneme: {result['phoneme']} (from word '{result['word']}'), Analysis: {result['feedback']}")
            if result['audio_file']:
                st.audio(result['audio_file'])

        # Generate suggestions for improvement
        if overall_similarity < 0.8:
            st.write("### Suggestions for Improvement")
            suggestions = generate_suggestions(analysis)
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

        # Save analysis results to a file
        analysis_results = {
            "expected_text": expected_text,
            "transcription": transcription,
            "analysis": analysis,
            "overall_similarity": overall_similarity,
            "phoneme_analysis": phoneme_analysis
        }
        with open("analysis_results.json", "w") as f:
            json.dump(analysis_results, f)

        # Remove the temporary files
        os.remove("uploaded_video.mp4")
        os.remove(audio_file_path)
        os.remove("temp_audio_mono.wav")
        for result in phoneme_analysis:
            if os.path.exists(result['audio_file']):
                os.remove(result['audio_file'])
        
        st.markdown('</div>', unsafe_allow_html=True)

elif tab == "Train Yourself":
    display_train_yourself()

elif tab == "Send Report":
    send_report()

# Instructions on how to run the app
st.markdown("""
### How to run this app:
- Save this script in your project directory.
- Open a terminal, navigate to the project directory, and run streamlit run app.py.
- Your app will open in a new tab in your web browser.
""")
