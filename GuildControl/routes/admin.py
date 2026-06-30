from flask import Blueprint, render_template, request, redirect, url_for

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/servicos")
def configurar_servicos():
    return render_template("servicos.html")

@admin_bp.route("/criar_squad", methods=["POST"])
def criar_squad():
    if request.method == "POST":
        nome_linha = request.form.get("nome_linha")
        descricao_linha = request.form.get("descricao_linha")
        
        # Lógica para o Bot criar a linha automaticamente
        print(f"Bot criando squad: {nome_linha}")
        
        return redirect(url_for("admin.configurar_servicos"))
