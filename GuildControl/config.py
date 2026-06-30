```python
import os

class Config:
    # Chave secreta para criptografia de sessões e logins
    SECRET_KEY = os.environ.get("SECRET_KEY", "guildcontrol2026")
    
    # Caminho oficial do banco de dados apontando para a pasta que você mostrou
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", 
        f"sqlite:///{os.path.join(BASE_DIR, 'database', 'database.db')}"
    )
    
    # Desativa notificações pesadas do banco para o site rodar mais rápido
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
