import sqlite3
from sqlite3 import Cursor

class Produto():
    def __init__(self, nome, preco, quantidade):
        self.name = nome
        self.preco = preco
        self.quantidade = quantidade

    def consultar_produto(cursor: Cursor, nome):
        dados_do_produto = cursor.execute("SELECT id, nome, preco, quantidade FROM produtos WHERE nome = ?", (nome,)).fetchone()

        if not dados_do_produto:
            return {"status": False, "produto": None, "mensagem": "Produto não encontrado!"}
        
        produto = {"Id": dados_do_produto[0],
                   "Nome": dados_do_produto[1],
                   "Preco": dados_do_produto[2],
                   "Quantidade": dados_do_produto[3]
                   }

        return {"status": True, "produto": produto, "mensagem": "Produto encontrado!"}

    def atualizar_quantidade(cursor: Cursor, nome, quantidade):
        produto_existe = Produto.consultar_produto(cursor, nome)
        
        if not produto_existe["status"]:
            print(produto_existe["mensagem"])
            return

        atualiza_produto = cursor.execute("UPDATE produtos SET quantidade = ? WHERE nome = ?", (quantidade, nome))
        cursor.connection.commit()

        return {"mensagem": "Produto atualizado com sucesso!"}

    def criar_produto(cursor: Cursor, nome, preco, quantidade):
        resultado_validacao = {"status": True, "mensagem": "Produto criado com sucesso!"}

        if not isinstance(nome, str) or not nome.strip():
            resultado_validacao["status"] = False
            resultado_validacao["mensagem"] = "O nome deve ser uma string não vazia."
            return resultado_validacao

        if not isinstance(preco, (int, float)) or preco <= 0:
            resultado_validacao["status"] = False
            resultado_validacao["mensagem"] = "O preço deve ser um número positivo."
            return resultado_validacao
        
        if not isinstance(quantidade, int) or quantidade < 0:
            resultado_validacao["status"] = False
            resultado_validacao["mensagem"] = "A quantidade deve ser um inteiro não negativo."
            return resultado_validacao
        
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
        cursor.connection.commit()

        return resultado_validacao

def create_app():
    db = sqlite3.connect("produtos.db")
    
    cursor= db.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS produtos (
              id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              nome TEXT NOT NULL,
              preco FLOAT NOT NULL,
              quantidade INTEGER NOT NULL
              )
              """)

    while(True):
        print("Escolha uma ação: ")
        print("[1] Consultar produto")
        print("[2] Atualizar quantidade")
        print("[3] Criar produto")
        
        acao = int(input("Digite: "))
        
        match(acao):
            case 1:
                nome = input("Qual o nome do produto que você deseja consultar: ")
                produto_dados = Produto.consultar_produto(cursor, nome=nome)
                
                if not produto_dados["status"]:
                    print(produto_dados["mensagem"])
                    continue

                for dados in produto_dados["produto"]:
                    coluna = dados
                    dados_coluna = produto_dados["produto"][dados]
                    print(f"{coluna}: {dados_coluna}")
            
            case 2:
                nome = input("Qual produto você deseja atualizar: ")
                quantidade = input("Qual é a nova quantidade: ")
                
                atualiza_produto = Produto.atualizar_quantidade(cursor, nome=nome,quantidade=quantidade)
                db.commit()
                print(atualiza_produto["mensagem"])

            case 3:
                nome = input("Nome: ")
                preco = float(input("Preco: "))
                quantidade = int(input("Quantidade: "))
                
                produtoCriado = Produto.criar_produto(cursor, nome, preco, quantidade)

                print(produtoCriado["mensagem"])
            case _:
                print("Operação não válida no sistema!")

if __name__ == "__main__":
    create_app()