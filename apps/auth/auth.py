from flask import session, redirect, url_for, request, render_template
from functools import wraps


def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'usuario' in session:
                if not session['nivel_acesso'] == role:
                    return render_template('erro404.html')
                    #session['url_atual'] = request.path # verificar depois se esse código está funcionando

                return f(*args, **kwargs)

                # return redirect(session['next_url'])
            return redirect(url_for('auth_bp.login'))

        return decorated_function

    return decorator

def is_autorizad():
    pass