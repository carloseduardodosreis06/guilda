```python
from flask import Blueprint, render_template, request, redirect, url_for

membros_bp = Blueprint('membros', __name__)

@membros_bp.route("/membros")
def gerenciar_membros():
    return render_template("dashboard.html") # Se você preferir, pode redirecionar para guilda

@membros_bp.route("/adicionar_membro", methods=["POST"])
def adicionar_membro():
    if request.method == "POST":
        line = request.form.get("line")
        slot = request.form.get("slot")
        nick = request.form.get("nick")
        id_jogo = request.form.get("id_jogo")
        telefone = request.form.get("telefone")
        
        # Aqui os dados serão salvos no banco de dados futuramente
        print(f"Adicionando {nick} no Slot {slot} da {line}")
        
        return redirect(url_for("guildas.visualizar_guilda"))
```
("planos.pagamentos"))
