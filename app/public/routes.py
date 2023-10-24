from . import _public
from flask import render_template

@_public.route("/")
def login():
    return render_template('Login.html', title='Login')

@_public.route('/home')
def index():
    return render_template('home.html', title='Home')