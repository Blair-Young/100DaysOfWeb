from program import app
from flask import render_template, request
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

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
	pokemon = []
	if request.method == 'POST' and 'pokecolour' in request.form:
		colour = request.form.get('pokecolour')
		pokemon = get_pokemon_based_on_color(colour)
		if pokemon:
			return render_template('pokemon.html', pokemon=pokemon, error=None)
		return render_template('pokemon.html', pokemon=None, error=400)
	elif request.method == 'POST' and 'pokename' in request.form:
		name = request.form.get('pokename')
		coolpoke = get_is_it_a_cool_pokemon(name)
		print(coolpoke)
		return render_template('pokemon.html', coolpoke=coolpoke)
	return render_template('pokemon.html')


def get_pokemon_based_on_color(colour):
	valid_colours = ['red', 'blue', 'brown', 'black', 'green', 'yellow']
	if colour in valid_colours:
		endpoint = f'https://pokeapi.co/api/v2/pokemon-color/{colour.lower()}/'
		r = requests.get(endpoint)
		pokemon = []
		for i in r.json()['pokemon_species']:
			pokemon.append(i['name'])
		return pokemon

def get_is_it_a_cool_pokemon(name):
	print(name)
	if name =='arcanine':
		return 'yes'
	return 'no'


def get_chuck_quote():
	r = requests.get('https://api.chucknorris.io/jokes/random')
	data = r.json()
	return data['value']










