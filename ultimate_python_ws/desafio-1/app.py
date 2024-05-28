from libs.database import Database
from models.user import User
from models.authenticator import Authenticator

def create_app():
    db = Database("users.db")
    db.users_table_init()
  
    authenticator = Authenticator()

    while(True):
        print("---- Entrar no Sistema ----")
        print("[1] Cadastre-se")
        print("[2] Fazer login")
        acao = int(input("Escolha uma ação: "))
        
        name = input("Usuário: ")
        password = input("Senha: ")
        
        match(acao):
            case 1:
                createUser = User.create_user(name, password)

                print(createUser["mensagem"])
                continue
            case 2:
                loginUser = authenticator.login(User(name, password))
                
                print(loginUser["mensagem"])
                return
            case _:
                print("Não temos essa ação no sistema!")   


if __name__ == "__main__":
    create_app()
