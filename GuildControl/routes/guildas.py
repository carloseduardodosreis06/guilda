from flask import Blueprint, render_template, request, redirect, url_for

guildas_bp = Blueprint('guildas', __name__)

@guildas_bp.route("/guilda")
def visualizar_guilda():
    return render_template("guilda.html")
