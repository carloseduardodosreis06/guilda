```python id="wq8k1m"
from flask import Flask, render_template, redirect, url_for

# Puxa a configuração e o banco de dados das suas respectivas pastas
from config import Config
from database.models import db

# Importa todas as rotas/blueprints que configuramos na pasta routes
from routes.auth import auth
from routes.guildas import guildas_bp
from routes.membros import membros_bp
from routes.planos import planos_bp
from routes.pontuacoes import pontuacoes_bp
from routes.admin import admin_bp

def create_app():
    app = Flask(__name__)
    
    # Carrega as configurações oficiais do arquivo config.py
    app.config.from_object(Config)
    
    # Inicializa o banco de dados integrado ao Flask
    db.init_app(app)
    
    # REGISTRA TODOS OS BLUEPRINTS DAS SUAS ROTAS
    app.register_blueprint(auth)
    app.register_blueprint(guildas_bp)
    app.register_blueprint(membros_bp)
    app.register_blueprint(planos_bp)
    app.register_blueprint(pontuacoes_bp)
    app.register_blueprint(admin_bp)
    
    # ROTA PRINCIPAL DO PAINEL / DASHBOARD
    @app.route("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    # ROTA ESPECÍFICA PARA O PERFIL INDIVIDUAL
    @app.route("/perfil")
    def perfil():
        return render_template("perfil.html")

    # CRIA AS TABELAS AUTOMATICAMENTE SE NÃO EXISTIREM NO BANCO
    with app.app_context():
        db.create_all()
        
    return app

# Cria a instância oficial que o Gunicorn e o Render vão ler
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```
