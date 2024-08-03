from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Usuario, Lotacao
from app.database import db
from app.modulos.auth.auth import login_required

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin', template_folder='templates')

@admin_bp.route('/')
@login_required('master')
def home():
    return render_template('admin/index.html')

@admin_bp.route('/usuarios', methods=['GET', 'POST'])
@login_required('master')
def usuarios():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        email = request.form.get('email')
        lotacao = request.form.get('lotacao')
        nivel_acesso = request.form.get('nivel')
        ativo_str = request.form.get('ativo')
        ativo = True if ativo_str == 'true' else False

        usuario = Usuario(nome, sobrenome, usuario, senha, email, lotacao, nivel_acesso, ativo)
        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('admin_bp.usuarios'))

    usuarios = Usuario.query.all()
    lotacoes = Lotacao.query.all()
    return render_template('admin/usuarios.html', usuarios=usuarios, lotacoes=lotacoes)

@admin_bp.route('/usuarios/excluir/<int:id>')
@login_required('master')
def excluir_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario excluído com sucesso!')
        return redirect(url_for('admin_bp.usuarios'))

    flash('Usuario não encontrado')

'''
AQUI ESTÁ CÓDIFICADO AS ROTAS DE LISTAR, EXCLUIR E EDITAR AS
LOTAÇÕES DOS USUÁRIO DO SISTEMA, ESTAS FUNCIONALIDADES ESTÃO 
DESCRITAS NA ÁREA DE ADMINISTRAÇÃO 
'''

@admin_bp.route('/lotacao', methods=['GET', 'POST'])
@login_required('master')
def lotacao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        ativo_str = request.form.get('ativo')
        ativo = True if ativo_str == 'true' else False

        lotacao = Lotacao(nome, ativo)
        db.session.add(lotacao)
        db.session.commit()

        flash('dados de lotação cadastrados com sucesso!')

        return redirect(url_for('admin_bp.lotacao'))

    lotacoes = Lotacao.query.all()
    return render_template('admin/lotacao.html', lotacoes=lotacoes)

@admin_bp.route('/lotacao/excluir/<int:id>')
@login_required('master')
def excluir_lotacao(id):
    lotacao = Lotacao.query.get(id)
    if lotacao:
        db.session.delete(lotacao)
        db.session.commit()

        flash('Lotação excluída com sucesso!')

        return redirect(url_for('admin_bp.lotacao'))

    flash('Lotação não encontrado')
    return redirect(url_for('admin_bp.lotacao'))

@admin_bp.route('/lotacao/editar/<int:id>')
@login_required('master')
def editar_lotacao(id):
    pass



