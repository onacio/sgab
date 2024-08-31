from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from apps.admin.models import Usuario

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and user.senha == senha:
            if user.ativo == 1:
                session['usuario'] = user.usuario
                session['nome'] = user.nome
                session['lotacao'] = user.lotacao
                session['nivel_acesso'] = user.nivel_acesso

                if session['nivel_acesso'] == 'master':
                    return redirect(url_for('admin_bp.home'))
                elif session['nivel_acesso'] == 'gestor':
                    return redirect(url_for('gestor_bp.home'))

                return redirect(url_for('home_bp.home'))
            else:
                flash('Acesso não autorizado', 'danger')
        else:
            flash('Usuário ou senha inválida!!!', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('nome', None)
    session.pop('lotacao', None)
    session.pop('nivel_acesso', None)
    session.pop('url_atual', None)
    return redirect(url_for('auth_bp.login'))