from libs.database import Database

db = Database("users.db")

class User():
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password
    
    def create_user(name, password):
        nameExists = db.execute_query("SELECT name FROM users WHERE name = ?", (name,)).fetchone()

        if nameExists:
            return {"status": False, "mensagem": "Usuários já cadastrado no sistema!"}
        
        db.execute_query("""
            INSERT INTO users (name, password) 
            VALUES (?, ?)
        """, (name, password))
        db.connection.commit()
        return {"status": True, "mensagem": "Usuário cadastrado com sucesso, faça login para iniciar sua sessão!"}
    
    def get_user_by_name(name):
        rowResultData = db.execute_query(f"""SELECT id, name, password FROM users 
                WHERE name == ?  
        """, (name,))

        result = rowResultData.fetchone()

        if result is None:
            return {"status": False, "user": None}
        
        user = {"id": result[0], "name": result[1], "password": result[2]}
        return {"status": True, "user": user }