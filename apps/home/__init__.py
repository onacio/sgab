from flask import Blueprint, render_template
from apps.auth.auth import login_required


home_bp = Blueprint('home_bp', __name__, template_folder='templates')

@home_bp.route('/')
@login_required('usuario')
def home():
    return render_template('home/index.html')

@home_bp.route('/sobre')
@login_required('usuario')
def sobre():
    return render_template('home/sobre.html')