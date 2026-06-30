```python
import datetime

class HorasService:
    @staticmethod
    def registrar_atividade_membro(id_jogo):
        """Gera um log com o dia e horário que o jogador logou ou pontuou"""
        horario_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[LOG ATIVIDADE] Jogador ID {id_jogo} ativo em: {horario_atual}")
        return horario_atual

    @staticmethod
    def calcular_tempo_line(horas_jogadas):
        """Valida se a line cumpriu a meta de horas mínimas estabelecidas"""
        meta_horas = 10
        if horas_jogadas >= meta_horas:
            return "Meta Cumprida ✓"
        return f"Pendente ({meta_horas - horas_jogadas}h restantes)"
```

    ]
