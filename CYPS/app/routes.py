# app/routes.py

from flask import current_app as app
from flask import render_template, request
from .crops import crops

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/crops')
def crops_page():
    return render_template('crops.html', crops=crops)

@app.route('/crops/<crop_name>')
def crop_detail(crop_name):
    crop = crops.get(crop_name)
    if crop:
        return render_template('crop.html', crop=crop)
    else:
        return render_template('404.html'), 404

@app.route('/blog')
def blog():
    return render_template('blog.html')
