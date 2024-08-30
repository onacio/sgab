from database import db
from datetime import date, time

class Pedidos(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True)            
    data = db.Column(db.Date, nullable=False, default=date.today)
    hora = db.Column(db.Time, nullable=False, default=lambda: time())
    descricao = db.Column(db.String(200))
    categoria = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    quantidade_liberada = db.Column(db.Integer)
    status = db.Column(db.Boolean, nullable=False)
    solicitante = db.Column(db.String(100))
    justificativa = db.Column(db.String(255))
    data_finalizacao = db.Column(db.Date, nullable=False, default=date.today)    

    def __init__(self, data, hora, descricao, categoria, quantidade, solicitante, justificativa, status=0):   
        self.data = data
        self.hora = hora     
        self.descricao = descricao
        self.categoria = categoria
        self.quantidade = quantidade
        self.status = status
        self.solicitante = solicitante
        self.justificativa = justificativa
        
    
class ItensPedido(db.Model):
    __tablename__ = 'itens_pedido'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200))
    categoria = db.Column(db.String(100))
    ativo = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, descricao, categoria, ativo):
        self.descricao = descricao
        self.categoria = categoria
        self.ativo = ativo

    def __repr__(self):
        return 'Item_pedido: {}'.format(self.descricao)   