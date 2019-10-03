from flask import Blueprint, render_template

from .extensions import db
from .models import User, CoinInquire

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/ask')
def ask():
    return render_template('ask.html')

@main.route('/respa')
def respa():
    return render_template('respa.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/coinInquire')
def coinInquire():
    return render_template('coinInquire.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/unrespaed')
def unrespaed():
    return render_template('unrespaed.html')

@main.route()
