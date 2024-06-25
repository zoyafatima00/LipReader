from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename
from utils import extract_audio_from_video, transcribe_audio_vosk, analyze_transcription, generate_suggestions

app = Flask(__name__)

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
        
        # Extract audio from video
        audio_file_path = extract_audio_from_video(video_file_path)
        
        # Transcribe audio
        transcription = transcribe_audio_vosk(audio_file_path)
        
        # Analyze transcription
        analysis, overall_similarity = analyze_transcription(transcription, expected_text)
        
        # Generate phoneme suggestions
        suggestions = generate_suggestions(analysis)

        analysis_results = {
            "filename": filename,
            "expected_text": expected_text,
            "transcription": transcription,
            "overall_similarity": overall_similarity,
            "analysis": analysis,
            "suggestions": suggestions
        }

        session['results'] = analysis_results  # Store results in session
        print("Session set:", session['results'])  # Debug print
        return redirect(url_for('report'))
    return render_template('expected_phrase.html', filename=filename)

@app.route('/report')
def report():
    results = session.get('results', None)
    print("Session retrieved:", results)  # Debug print
    if results is None:
        return redirect(url_for('home'))  # Redirect to home if no results found in session
    return render_template('report.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
    # jsgdhdhhdhd