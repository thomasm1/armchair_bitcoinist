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

@main.route('/answer')
def answer():
    return render_template('answer.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/coinInquire')
def coinInquire():
    return render_template('coinInquire.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/unanswered')
def unanswered():
    return render_template('unanswered.html')

@main.route()
