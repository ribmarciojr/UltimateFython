from .user import User

class Authenticator():
    def __init__(self):
        return
    
    def login(self, user_data: User):
        user = User.get_user_by_name(user_data.name)

        if not user["status"]:
            return {"status": False, "mensagem": user["mensagem"]}

        if user["user"]["password"] != user_data.password:
            return {"status": False, "mensagem": "Erro, nome ou senha inválido!"}
            
        return {"status": True, "mensagem": "Parabéns, você está conectado!"}
