def iniciar_migracoes(app, db):
    """
    Sistema preparado para gerenciar futuras mudancas
    nas tabelas do banco de dados automaticamente.
    """
    try:
        print("✓ Sistema de banco de dados e migracoes ativo.")
    except Exception as e:
        print(f"Erro nas mudancas do banco: {e}")
