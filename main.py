from flask import Flask
from app.database import db
from flask_migrate import Migrate

""" IMPORTES DAS BLUEPRINTS """
from app.modulos.auth import auth_bp
from app.modulos.admin import admin_bp
from app.modulos.gestor import gestor_bp
from app.modulos.home import home_bp


app = Flask(__name__, static_folder='app/static')

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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)