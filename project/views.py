from flask import render_template
from app import app, pages

@app.route('/')
def home():
    return render_template('site/index.html')
