from application import app
from flask import render_template, request, current_app

@app.route("/")
def index():
    
    return render_template('index.html')
