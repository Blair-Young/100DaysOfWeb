from program import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/different_page')
def different_page():
	return render_template('different_page.html')