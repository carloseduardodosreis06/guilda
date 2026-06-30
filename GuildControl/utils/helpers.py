from werkzeug.security import generate_password_hash, check_password_hash

class Helpers:
    @staticmethod
    def criptografar_senha(senha):
        """Transforma a senha em um código seguro antes de salvar no banco"""
        return generate_password_hash(senha)

    @staticmethod
    def verificar_senha(senha_criptografada, senha_digitada):
        """Valida se a senha digitada no login bate com a senha do banco"""
        return check_password_hash(senha_criptografada, senha_digitada)
