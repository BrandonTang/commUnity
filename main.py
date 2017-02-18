import os
import requests
import json
import hashlib
import pyrebase
import sqlite3 as sql
from flask import Flask, render_template, request, session, url_for, redirect, flash
from flask_googlemaps import GoogleMaps, Map

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
    # Maps Section
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)],
        style="height:60%;width:100%;margin-top:15%;"
    )
    # Firebase Connection
    # db = firebase.database()
    # all_users = db.child("users").get()
    # for user in all_users.each():
    #     print(user.key())
    #     print(user.val())
    # user_ids = db.child("users").shallow().get()
    return render_template('index.html', mymap=mymap)


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
