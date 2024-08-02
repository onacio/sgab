from flask import Blueprint, render_template
from app.modulos.auth.auth import login_required

gestor_bp = Blueprint('gestor_bp', __name__, url_prefix='/gestor')

@gestor_bp.route('/')
@login_required('gestor')
def home():
    return render_template('gestor/home.html')