from flask import Flask
from database import db
from flask_migrate import Migrate

""" IMPORTES DAS BLUEPRINTS """
from apps.auth import auth_bp
from apps.admin import admin_bp
from apps.gestor import gestor_bp
from apps.home import home_bp
from apps.marcacao import marcacao_bp
from apps.pedidos import pedidos_bp


app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = 'minha-chave'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

""" INICIALIZAÇÃO DAS BLUEPRINTS """
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(gestor_bp)
app.register_blueprint(home_bp)
app.register_blueprint(marcacao_bp)
app.register_blueprint(pedidos_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)