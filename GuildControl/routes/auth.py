```python
from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route("/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        if email and senha:
            # Aqui depois conectamos com seu banco de dados
            return redirect(url_for("auth.login"))
            
    return render_template("cadastro.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")
        
        if email == "admin@email.com" and senha == "123456": # Exemplo de teste
            return redirect(url_for("dashboard")) # Redireciona para o app.py principal
            
        return redirect(url_for("auth.login"))
        
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("auth.login"))
```

    return redirect(url_for("auth.login"))
