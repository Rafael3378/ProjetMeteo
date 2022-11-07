# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
#import json
import requests


app = Flask(__name__) #lignes decorateur

METEO_API_KEY = "NTB37PKZUG" # clés

if METEO_API_KEY is None:
    # URL de test :
    METEO_API_URL = "http://app.objco.com:8099/?account=XXXX&limit=6"
else:
    # URL avec clé :
    METEO_API_URL = "http://app.objco.com:8099/?account=" + METEO_API_KEY + "&limit=6"
# print("http://app.objco.com:8099/?account=" + METEO_API_KEY + "&limit=6")

@app.route("/") #lignes decorateur associe hello à /#
def hello():
    return "Hello World!"

@app.route('/api/meteo/')
def meteo():
    response = requests.get(METEO_API_URL)
    content = response.json()
    return content

if __name__ == "__main__":
    app.run(debug=True) #affiche si il y a une erreur dans le debogage