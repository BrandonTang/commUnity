import os
import hashlib
import sqlite3 as sql
from flask import Flask, render_template, request, session, url_for, redirect, flash

# Initialize the app from Flask
app = Flask(__name__)
app.secret_key = 'secret_key'


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Return the home page that displays all uploaded images and their captions.
    """
    logged_in = False
    if session.get('logged_in') is True:
        logged_in = True
    username = session.get('username')
    return render_template('index.html', logged_in=logged_in, username=username)


@app.route('/login')
def login():
    """
    Return the login page that calls login_auth on submit.
    """
    return render_template('login.html')


@app.route('/login_auth', methods=['GET', 'POST'])
def login_auth():
    """
    Authenticates user credentials, creates session for user if valid, else redirects to login with flash message.
    """
    username = request.form['username']
    password = request.form['password']
    md5password = hashlib.md5(password.encode('utf-8')).hexdigest()
    conn = sql.connect("appsec.db", timeout=10)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, md5password))
    user = cursor.fetchone()
    conn.commit()
    conn.close()
    if user:
        session['username'] = username
        session['logged_in'] = True
        flash('User successfully logged in!', category='success')
        return redirect(url_for('index'))
    else:
        flash('Invalid login or username or password.', category='error')
        return redirect(url_for('login'))


@app.route('/register')
def register():
    """
    Return the register page that calls register_auth on submit.
    """
    return render_template('register.html')


@app.route('/register_auth', methods=['GET', 'POST'])
def register_auth():
    """
    Checks if user already exists, redirects to register page if true, else creates new user.
    """
    username = request.form['username']
    password = request.form['password']
    md5password = hashlib.md5(password.encode('utf-8')).hexdigest()
    conn = sql.connect("appsec.db", timeout=10)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.commit()
    conn.close()
    if user:
        flash('User already exists.', category='error')
        return redirect(url_for('register'))
    else:
        insert_user(username, md5password)
        flash('User successfully registered! You may login now.', category='success')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """
    Logs out the user and removes information from session, then redirects to index page.
    """
    session.pop('username')
    session.pop('logged_in')
    flash('User successfully logged out.', category='success')
    return redirect('/')


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
