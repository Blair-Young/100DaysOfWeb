from program import app
from flask import render_template
import datetime
import requests

@app.route('/')
@app.route('/index')
def index():
	timenow = datetime.datetime.today()
	return render_template('index.html', time=timenow)

@app.route('/100days')
def p100days():
	return render_template('100days.html')

@app.route('/chuck')
def chuck():
	joke = get_chuck_quote()
	return render_template('chuck.html', joke=joke)


def get_chuck_quote():
	r = requests.get('https://api.chucknorris.io/jokes/random')
	data = r.json()
	return data['value']







