from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/worksheet')
def worksheet():
    return render_template('worksheet.html')

@app.route('/report')
def report():
    return "This is the report page."

if __name__ == '__main__':
    app.run(debug=True)
