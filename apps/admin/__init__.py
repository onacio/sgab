from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Usuario, Lotacao
from database import db
from apps.auth.auth import login_required

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin', template_folder='templates', static_folder='static')

@admin_bp.route('/')
@login_required('master')
def home():
    return render_template('admin/index.html')

@admin_bp.route('/usuarios', methods=['GET', 'POST'])
@login_required('master')
def usuarios():
    if request.method == 'POST':
        usuario_id = request.form.get('id')

        if usuario_id:
            usuario = Usuario.query.get(usuario_id)
            
            usuario.nome = request.form.get('nome')
            usuario.sobrenome = request.form.get('sobrenome')
            usuario.usuario = request.form.get('usuario')
            usuario.senha = request.form.get('senha')
            usuario.email = request.form.get('email')
            usuario.lotacao = request.form.get('lotacao')
            usuario.nivel_acesso = request.form.get('nivel')
            ativo_str = request.form.get('ativo')
            usuario.ativo = True if ativo_str == 'true' else False

            db.session.commit()
            
            flash('Usuário atualizado com sucesso!!!', 'success')
        else:            
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

            flash('Usuário cadastrado com sucesso!!!', 'success')

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
        flash('Usuario excluído com sucesso!', 'success')
        return redirect(url_for('admin_bp.usuarios'))

    flash('Usuario não encontrado', 'danger')

'''
AQUI ESTÁ CÓDIFICADO AS ROTAS DE LISTAR, EXCLUIR E EDITAR AS
LOTAÇÕES DOS USUÁRIO DO SISTEMA, ESTAS FUNCIONALIDADES ESTÃO 
DESCRITAS NA ÁREA DE ADMINISTRAÇÃO 
'''

@admin_bp.route('/lotacao', methods=['GET', 'POST'])
@login_required('master')
def lotacao():
    if request.method == 'POST':
        lotacao_id = request.form.get('id')
        
        if lotacao_id:
            lotacao = Lotacao.query.get(lotacao_id)

            lotacao.nome = request.form.get('nome')
            ativo_str = request.form.get('ativo')
            lotacao.ativo = True if ativo_str == 'true' else False

            db.session.commit()

            flash('Lotação atualizada com sucesso!!!', 'success')
        else:
            nome = request.form.get('nome')
            ativo_str = request.form.get('ativo')
            ativo = True if ativo_str == 'true' else False

            lotacao = Lotacao(nome, ativo)
            db.session.add(lotacao)
            db.session.commit()

            flash('Lotação cadastrada com sucesso!!!', 'success')

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

        flash('Lotação excluída com sucesso!', 'success')

        return redirect(url_for('admin_bp.lotacao'))

    flash('Lotação não encontrado', 'danger')
    return redirect(url_for('admin_bp.lotacao'))