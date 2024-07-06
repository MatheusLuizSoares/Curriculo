from . import db
from datetime import datetime

class Curriculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cargo_desejado = db.Column(db.String(100), nullable=False)
    escolaridade = db.Column(db.String(50), nullable=False)
    observacoes = db.Column(db.Text, nullable=True)
    arquivo = db.Column(db.String(120), nullable=True)
    ip = db.Column(db.String(45), nullable=False)
    data_envio = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
