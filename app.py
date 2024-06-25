# from flask import Flask, render_template, request, redirect, url_for, session
# import os
# from werkzeug.utils import secure_filename
# from utils import extract_audio_from_video, transcribe_audio_vosk, analyze_transcription, generate_suggestions, get_phoneme_analysis
# import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'
# app.secret_key = 'supersecretkey'  # Ensure this is set for session management
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# def basename(path):
#     return os.path.basename(path)

# app.jinja_env.filters['basename'] = basename

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/worksheet')
# def worksheet():
#     return render_template('worksheet.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#         if file:
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('analyze_file', filename=filename))
#     return render_template('upload.html')

# # @app.route('/analyze/<filename>', methods=['GET', 'POST'])
# # def analyze_file(filename):
# #     if request.method == 'POST':
# #         expected_text = request.form['expected_text']
# #         video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
# #         # Extract audio from video
# #         audio_file_path = extract_audio_from_video(video_file_path)
        
# #         # Transcribe audio
# #         transcription = transcribe_audio_vosk(audio_file_path)
        
# #         # Analyze transcription
# #         analysis, overall_similarity = analyze_transcription(transcription, expected_text)
        
# #         # Generate phoneme suggestions
# #         suggestions = generate_suggestions(analysis)

# #         phoneme_analysis = get_phoneme_analysis(transcription)

# #         analysis_results = {
# #             "filename": filename,
# #             "expected_text": expected_text,
# #             "transcription": transcription,
# #             "overall_similarity": overall_similarity,
# #             "analysis": analysis,
# #             "suggestions": suggestions,
# #             "phoneme_analysis": phoneme_analysis  # Include phoneme analysis results
# #         }

# #         session['results'] = analysis_results  # Store results in session
# #         print("Session set:", session['results'])  # Debug print
# #         return redirect(url_for('report'))
# #     return render_template('expected_phrase.html', filename=filename)
# @app.route('/analyze/<filename>', methods=['GET', 'POST'])
# def analyze_file(filename):
#     if request.method == 'POST':
#         expected_text = request.form['expected_text']
#         video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
#         logging.info(f'Analyzing file: {filename}')
#         logging.debug(f'Expected text: {expected_text}')
        
#         try:
#             # Extract audio from video
#             audio_file_path = extract_audio_from_video(video_file_path)
#             logging.info(f'Audio extracted: {audio_file_path}')
            
#             # Transcribe audio
#             transcription = transcribe_audio_vosk(audio_file_path)
#             logging.info(f'Transcription: {transcription}')
            
#             # Analyze transcription
#             analysis, overall_similarity = analyze_transcription(transcription, expected_text)
#             logging.info(f'Analysis: {analysis}')
#             logging.info(f'Overall similarity: {overall_similarity}')
            
#             # Generate phoneme suggestions
#             suggestions = generate_suggestions(analysis)
#             logging.info(f'Suggestions: {suggestions}')
            
#             # Get phoneme analysis
#             phoneme_analysis = get_phoneme_analysis(transcription)
#             logging.info(f'Phoneme analysis: {phoneme_analysis}')
            
#             analysis_results = {
#                 "filename": filename,
#                 "expected_text": expected_text,
#                 "transcription": transcription,
#                 "overall_similarity": overall_similarity,
#                 "analysis": analysis,
#                 "suggestions": suggestions,
#                 "phoneme_analysis": phoneme_analysis
#             }

#             session['results'] = analysis_results  # Store results in session
#             logging.info(f'Results stored in session: {session["results"]}')
#             return redirect(url_for('report'))
#         except Exception as e:
#             logging.error(f'Error during analysis: {e}')
#             return redirect(url_for('upload'))
#     return render_template('expected_phrase.html', filename=filename)


# @app.route('/report')
# def report():
#     results = session.get('results', None)
#     print("Session retrieved:", results)  # Debug print
#     if results is None:
#         return redirect(url_for('home'))  # Redirect to home if no results found in session
#     return render_template('report.html', results=results)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
from werkzeug.utils import secure_filename
from utils import extract_audio_from_video, transcribe_audio_vosk, analyze_transcription, generate_suggestions, get_phoneme_analysis
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'supersecretkey'  # Ensure this is set for session management
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def basename(path):
    return os.path.basename(path)

app.jinja_env.filters['basename'] = basename

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/worksheet')
def worksheet():
    return render_template('worksheet.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('analyze_file', filename=filename))
    return render_template('upload.html')

@app.route('/analyze/<filename>', methods=['GET', 'POST'])
def analyze_file(filename):
    if request.method == 'POST':
        expected_text = request.form['expected_text']
        video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        audio_file_path = extract_audio_from_video(video_file_path)
        #logging.info(f'Audio extracted: {audio_file_path}')
        
        # Transcribe audio
        transcription = transcribe_audio_vosk(audio_file_path)
        # logging.info(f'Transcription: {transcription}')
        
        # Analyze transcription
        analysis, overall_similarity = analyze_transcription(transcription, expected_text)
        # logging.info(f'Analysis: {analysis}')
        # logging.info(f'Overall similarity: {overall_similarity}')
        
        # Generate phoneme suggestions
        suggestions = generate_suggestions(analysis)
        # logging.info(f'Suggestions: {suggestions}')
        
        # Get phoneme analysis
        phoneme_analysis = get_phoneme_analysis(transcription)
        # logging.info(f'Phoneme analysis: {phoneme_analysis}')
        

        analysis_results = {
            "filename": filename,
            "expected_text": expected_text,
            "transcription": transcription,
            "overall_similarity": overall_similarity,
            "analysis": analysis,
            "suggestions": suggestions,
            "phoneme_analysis": phoneme_analysis
        }

        session['results'] = analysis_results  # Store results in session
        print("Session set:", session['results'])  # Debug print
        return render_template('analyze.html', results=analysis_results)
    return render_template('expected_phrase.html', filename=filename)

@app.route('/report')
def report():
    results = session.get('results', None)
    print("Session retrieved:", results)  # Debug print
    if results is None:
        return redirect(url_for('home'))  # Redirect to home if no results found in session
    return render_template('report.html', results=results)

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory('static/audio', filename)

if __name__ == '__main__':
    app.run(debug=True)
