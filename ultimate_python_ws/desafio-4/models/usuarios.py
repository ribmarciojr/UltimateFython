from sqlite3 import Cursor

class Usuario():
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

    def cadastrar_usuario(cursor: Cursor, nome, senha):
        user = cursor.execute("SELECT nome FROM users WHERE nome = ?", (nome,)).fetchone()
        if user:
            return {"status": False, "mensagem": "Tente outro nome de usuário!"}
        
        cursor.execute("INSERT INTO users (nome, senha) VALUES (?, ?)", (nome, senha))

        cursor.connection.commit()

        return {"status": True, "mensagem": "Usuário cadastrado!"}
    def login(cursor: Cursor, nome, senha):
        user = cursor.execute("SELECT nome, senha FROM users WHERE nome = ?", (nome,)).fetchone()
        if not user:
            return {"status": False, "mensagem": "Usuário não existente!"}

        if user[1] != senha:
            return {"status": False, "mensagem": "Senha incorreta!"}
        
        return {"status": True, "mensagem": "Usuário logado!"}