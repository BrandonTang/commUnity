import os
import requests
import json
import hashlib
import pyrebase
import sqlite3 as sql
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_googlemaps import GoogleMaps, Map, icons

# Initialize the app from Flask
app = Flask(__name__)
app.secret_key = 'secret_key'

config = {
    "apiKey": "AIzaSyAouz-Hjy7z8fu-8zIlYs4Ay4tfLURAUYw",
    "authDomain": "chalkitup-5b411.firebaseapp.com",
    "databaseURL": "https://chalkitup-5b411.firebaseio.com",
    "storageBucket": "chalkitup-5b411.appspot.com",
    "messagingSenderId": "933786712703"
}

firebase = pyrebase.initialize_app(config)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyA7PFRZw7yC2TcwR0Rm8k8V0l-MSZt4aRk"
GoogleMaps(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return the home page for commUnity that displays about, download, team, and maps sections.
    """
    # Firebase Connection
    # db = firebase.database()
    # all_users = db.child("users").get()
    # for user in all_users.each():
    #     print(user.key())
    #     print(user.val())
    # user_ids = db.child("users").shallow().get()
    # Maps Section
    mymap = Map(
        identifier="sndmap",
        zoom=16,
        lat=40.6939904,
        lng=-73.98656399999999,
        # markers=[(40.6939904,-73.98656399999999)],
        # markers=[
        #     {
        #         'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
        #         'lat': 40.6939904,
        #         'lng': -73.98656399999999,
        #         'infobox': "<b>Current Location</b>"
        #     },
        #     {
        #         'icon': 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
        #         'lat': 40.693364,
        #         'lng': -73.98571470000002,
        #         'infobox': "<b>Five Guys</b>"
        #     }
        # ],
        markers={icons.dots.green: [(40.693364, -73.98571470000002, "Five Guys")],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(40.6939904, -73.98656399999999, "Current Location")]},
        style="height:60%;width:100%;margin-top:15%;"
    )
    return render_template('index.html', mymap=mymap)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
