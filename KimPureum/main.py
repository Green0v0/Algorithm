from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/01_basic')
def basic():
    html = render_template('01_basic.html')
    return html

@app.route('/02_header')
def header():
    html = render_template('02_header.html')
    return html

@app.route('/03_paragraphs')
def paragraphs():
    html = render_template('03_paragraphs.html')
    return html\

@app.route('/04_link')
def link():
    html = render_template('04_link.html')
    return html

@app.route('/05_Table')
def Table():
    html = render_template('05_Table.html')
    return html

@app.route('/06_List')
def List():
    html = render_template('06_List.html')
    return html


app.run(host='0.0.0.0', port=80, debug=True)