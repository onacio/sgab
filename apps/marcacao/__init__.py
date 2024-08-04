from flask import Blueprint, render_template, request, redirect, url_for
from apps.marcacao.models import Marcacao
from database import db
from datetime import datetime


marcacao_bp = Blueprint('marcacao_bp', __name__, url_prefix='/marcacao', template_folder='templates')


@marcacao_bp.route('/')
def home():
    marcacoes = Marcacao.query.all()
    return render_template('marcacao/index.html', marcacoes=marcacoes)

@marcacao_bp.route('/inserir', methods=['POST'])
def inserir_marcacao():
    tipo = request.form.get('tipo')
    medico = request.form.get('medico')

    data_str = request.form.get('data')
    data = datetime.strptime(data_str, "%Y-%m-%d")

    vagas = request.form.get('vagas')

    marcacao = Marcacao(tipo, medico, data, vagas)
    db.session.add(marcacao)
    db.session.commit()

    return redirect(url_for('marcacao_bp.home'))

@marcacao_bp.route('/inserir-agendamento', methods=['POST'])
def inserir_agendamento():
    nome_paciente = request.form.get('nome_paciente')
    return