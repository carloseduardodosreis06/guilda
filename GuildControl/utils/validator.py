import re

class Validator:
    @staticmethod
    def validar_email(email):
        """Verifica se o formato do e-mail é válido no cadastro"""
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(padrao, email):
            return True
        return False

    @staticmethod
    def limpar_e_validar_id(id_jogo):
        """Remove letras e garante que o ID do jogo contenha apenas números"""
        id_limpo = re.sub(r'\D', '', str(id_jogo))
        if len(id_limpo) >= 5:
            return id_limpo
        return None
