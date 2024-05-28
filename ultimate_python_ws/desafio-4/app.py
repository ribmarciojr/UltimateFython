import sqlite3
from models.produto import Produto
from models.transacao import Transacao
from models.usuarios import Usuario
    
def create_app():
    db = sqlite3.connect("ecommerce.db")

    cursor = db.cursor()

    db.execute("""CREATE TABLE IF NOT EXISTS users (
        if INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL   
        )
        """)

    db.execute("""CREATE TABLE IF NOT EXISTS produtos (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT NOT NULL,
        preco FLOAT NOT NULL,
        quantidade INTEGER NOT NULL       
        )
        """)
    
    db.execute("""CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        codigo_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL
        )""")

    login = False
    while(True):
        print("---- Entrar no Sistema ----")
        print("[1] Cadastre-se")
        print("[2] Fazer login")
        acao = int(input("Digite: "))
        
        nome = input("Usuário: ")
        senha = input("Senha: ")

        match(acao):
            case 1:
                createUser = Usuario.cadastrar_usuario(cursor, nome, senha)

                print(createUser["mensagem"])
                db.commit()
            case 2:
                loginUser = Usuario.login(cursor, nome, senha)
                login = loginUser["status"]
                print(loginUser["mensagem"])
                
                if login:
                    break
    while(login):
        print("---- Acões do sistema ----")
        print("[1] Realizar venda")
        print("[2] Verificar estoque")
        print("[3] Cadastrar produto")
        print("[4] Relatório de vendas")
        print("[5] Atualizar produto")
        acao = int(input("Digite: "))

        match(acao):
            case 1:
                nome = input("Produto: ")
                quantidade = int(input("Quantidade: "))
                compra = Transacao.comprar(cursor, nome, quantidade)

                print(compra["mensagem"])
            case 2:
                estoque = Produto.verificar_estoque(cursor)
                
                print(estoque)
            case 3:
                nome = input("Nome: ")
                preco = float(input("Preco: "))
                quantidade = int(input("Quantidade: "))
        
                produto = Produto.criar_produto(cursor, nome, preco, quantidade)

                print(produto["mensagem"])
            case 4:
                vendas = Transacao.relatorio(cursor)

                print(vendas)
            case 5: 
                codigo = int(input("Código: "))
                nova_quantidade = int(input("Nova quantidade: "))
                
                atualizaProduto = Produto.atualizar_produto(cursor, codigo, nova_quantidade)

                print(atualizaProduto["mensagem"])
    return 

if __name__ == "__main__":
    create_app()