from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from app.modulos.admin.models import Usuario

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        user = Usuario.query.filter_by(usuario=usuario).first()

        print(user)

        if user and user.senha == senha:
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
            flash('Usuário ou senha inválida!!!')

    return render_template('auth/login.html')
@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('nome', None)
    session.pop('lotacao', None)
    session.pop('nivel_acesso', None)
    session.pop('url_atual', None)
    return redirect(url_for('auth_bp.login'))