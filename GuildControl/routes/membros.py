from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.models import db, MembroGuilda

membros_bp = Blueprint('membros', __name__)

@membros_bp.route("/membros")
def gerenciar_membros():
    membros = MembroGuilda.query.all()
    return render_template("dashboard.html", membros=membros)

@membros_bp.route("/adicionar_membro", methods=["POST"])
def adicionar_membro():
    if request.method == "POST":
        line = request.form.get("line")
        slot = request.form.get("slot")
        nick = request.form.get("nick")
        id_jogo = request.form.get("id_jogo")
        telefone = request.form.get("telefone")
        
        # Verifica se o ID do jogo já está cadastrado para não duplicar
        membro_existente = MembroGuilda.query.filter_by(id_jogo=id_jogo).first()
        if miembro_existente:
            flash("Este ID de Jogo já está cadastrado!", "danger")
            return redirect(url_for("guildas.visualizar_guilda"))
            
        # Salva o novo membro no banco de dados de verdade
        novo_membro = MembroGuilda(
            line=line,
            slot=int(slot) if slot else 1,
            nick=nick,
            id_jogo=id_jogo,
            telefone=telefone
        )
        
        db.session.add(novo_membro)
        db.session.commit()
        flash("Membro adicionado com sucesso!", "success")
        
    return redirect(url_for("guildas.visualizar_guilda"))
