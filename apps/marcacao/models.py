from database import db


class Marcacao(db.Model):
    __tablename__ = 'marcacao'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150), nullable=False)
    medico = db.Column(db.String(150), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    agendamentos = db.relationship('Agendamento', backref='marcacao', lazy=True)

    def __init__(self, tipo, medico, data, vagas):
        self.tipo = tipo
        self.medico = medico
        self.data = data
        self.vagas = vagas

class Agendamento(db.Model):
    __tablename__ = 'agendamento'
    id = db.Column(db.Integer, primary_key=True)
    nome_paciente = db.Column(db.String(150), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    marcacao_id = db.Column(db.Integer, db.ForeignKey('marcacao.id'), nullable=False)

    def __init__(self, nome_paciente, usuario_id, marcacao_id):
        self.nome_paciente = nome_paciente
        self.usuario_id = usuario_id
        self.marcacao_id = marcacao_id
