# routes/auth.py

from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint("auth", __name__)

@auth.route("/")
def cadastro():
    return render_template("cadastro.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        if email and senha:
            return redirect(url_for("dashboard"))

        return redirect(url_for("auth.login"))
        
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return redirect(url_for("auth.login"))
