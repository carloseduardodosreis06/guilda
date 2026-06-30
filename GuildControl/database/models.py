```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabela de Usuários (Quem faz login e cadastro no sistema)
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    plano = db.Column(db.String(50), default="Grátis")

# Tabela dos Membros da Guilda (Os slots das lines, ex: "Junio")
class MembroGuilda(db.Model):
    __tablename__ = 'membros_guilda'
    id = db.Column(db.Integer, primary_key=True)
    nick = db.Column(db.String(100), nullable=False)
    id_jogo = db.Column(db.String(50), unique=True, nullable=False)
    telefone = db.Column(db.String(30), nullable=False)
    line = db.Column(db.String(50), nullable=False)  # Ex: line1, line2
    slot = db.Column(db.Integer, nullable=False)     # 1, 2, 3 ou 4
    honra = db.Column(db.Integer, default=0)
    guerra = db.Column(db.Integer, default=0)

# Tabela de Squads criados pela Automação do Bot
class SquadBot(db.Model):
    __tablename__ = 'squads_bot'
    id = db.Column(db.Integer, primary_key=True)
    nome_linha = db.Column(db.String(100), nullable=False)
    descricao_linha = db.Column(db.Text, nullable=True)
```
