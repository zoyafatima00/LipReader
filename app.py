from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/worksheet')
def worksheet():
    return render_template('worksheet.html')

@app.route('/report')
def report():
    return "This is the report page."

if _name_ == '_main_':
    app.run(debug=True)