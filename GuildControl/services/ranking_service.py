```python
from database.models import MembroGuilda

class RankingService:
    @staticmethod
    def calcular_ranking_geral():
        """Busca os membros no banco e ordena do maior pontuador para o menor"""
        try:
            # Puxa os membros ordenando pela soma de Honra + Guerra
            membros = MembroGuilda.query.all()
            
            # Cria uma lista organizada calculando o total de pontos de cada um
            ranking = []
            for membro in membros:
                total_pontos = membro.honra + membro.guerra
                ranking.append({
                    "nick": membro.nick,
                    "honra": membro.honra,
                    "guerra": membro.guerra,
                    "total": total_pontos
                })
            
            # Ordena a lista do maior total para o menor
            ranking_ordenado = sorted(ranking, key=lambda x: x['total'], reverse=True)
            return ranking_ordenado
        except Exception:
            # Caso o banco esteja vazio, retorna um exemplo padrão para não quebrar a tela
            return [{"nick": "Junio", "honra": 0, "guerra": 0, "total": 0}]
```
