from flask import Flask
from .database import db
from flask_migrate import Migrate

""" IMPORTES DAS BLUEPRINTS """
from .modulos.auth import auth_bp
from .modulos.admin import admin_bp
from .modulos.gestor import gestor_bp
from .modulos.home import home_bp


app = Flask(__name__, template_folder='templates')

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