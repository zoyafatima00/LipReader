from moviepy.editor import VideoFileClip
import wave
from vosk import Model, KaldiRecognizer
import json
import os
from difflib import SequenceMatcher
from pydub import AudioSegment

def extract_audio_from_video(video_file_path):
    video_clip = VideoFileClip(video_file_path)
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path, codec='pcm_s16le')
    video_clip.close()
    return audio_path

def convert_audio_to_required_format(audio_file_path):
    sound = AudioSegment.from_file(audio_file_path)
    sound = sound.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    temp_audio_path = "converted_temp_audio.wav"
    sound.export(temp_audio_path, format="wav")
    return temp_audio_path

def transcribe_audio_vosk(audio_file_path):
    vosk_model_path = "vosk-model-small-en-us-0.15"  # Update this path if necessary
    if not os.path.exists(vosk_model_path):
        raise Exception(f"Model path {vosk_model_path} does not exist")
    
    try:
        vosk_model = Model(vosk_model_path)
    except Exception as e:
        raise Exception(f"Failed to create a model. Error: {str(e)}")

    converted_audio_path = convert_audio_to_required_format(audio_file_path)
    
    wf = wave.open(converted_audio_path, "rb")
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
    text = ' '.join([json.loads(res)["text"] for res in transcription])
    wf.close()
    os.remove(converted_audio_path)  # Clean up the temporary converted audio file
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

def generate_phoneme_feedback(phoneme):
    # Placeholder: Implement feedback generation logic here
    return f"Feedback for phoneme '{phoneme}'"

def generate_suggestions(analysis):
    suggestions = []
    for item in analysis:
        if item['similarity'] < 0.8:
            phoneme_feedback = generate_phoneme_feedback(item['expected'][0])
            suggestion = f"Improve the pronunciation of '{item['expected']}'. {phoneme_feedback}"
            suggestions.append(suggestion)
    return suggestions
