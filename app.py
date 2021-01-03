from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
import requests
from keys import CONSUMER_KEY, CONSUMER_SECRET

base_url = 'http://www.mapquestapi.com/geocoding/v1/address'
resp = requests.get(base_url, params={'key': CONSUMER_KEY, 'location': 'Martinez, CA'})

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECT'] = False
app.config['SECRET_KEY'] = 'mapquestrules'

@app.route
def show_homepage():
    pass