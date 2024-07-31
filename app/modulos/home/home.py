from flask import Blueprint, render_template

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    return render_template('home/index.html')

@home_bp.route('/sobre')
def sobre():
    return render_template('home/sobre.html')