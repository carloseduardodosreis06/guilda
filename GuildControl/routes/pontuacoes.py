```python
from flask import Blueprint, render_template

pontuacoes_bp = Blueprint('pontuacoes', __name__)

@pontuacoes_bp.route("/ranking")
def ver_ranking():
    return render_template("ranking.html")
```
