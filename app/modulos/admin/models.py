from app.database import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=True)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=True)
    lotacao = db.Column(db.String(100), nullable=False)
    nivel_acesso = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, nome, sobrenome, usuario, senha, email, lotacao, nivel_acesso, ativo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.usuario = usuario
        self.senha = senha
        self.email = email
        self.lotacao = lotacao
        self.nivel_acesso = nivel_acesso
        self.ativo = ativo

    def __repr__(self):
        return 'Usuario: {}'.format(self.nome)

class Lotacao(db.Model):
    __tablename__ = 'lotacao'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, nome, ativo):
        self.nome = nome
        self.ativo = ativo