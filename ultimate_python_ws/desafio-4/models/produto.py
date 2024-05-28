from sqlite3 import Cursor
class Produto():
    def __init__(self, nome, preco, quantidade, codigo=None):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def validar(self):
        if not isinstance(self.nome, str) or not self.nome.strip():
            return {"status": False, "mensagem": "O nome deve ser uma string não vazia."}

        if not isinstance(self.preco, (int, float)) or self.preco <= 0:
            return {"status": False, "mensagem": "O preço deve ser um número positivo."}
        
        if not isinstance(self.quantidade, int) or self.quantidade < 0:
            return {"status": False, "mensagem": "A quantidade deve ser um inteiro não negativo."}

        return {"status": True, "mensagem": "Produto criado com sucesso!"}

    def criar_produto(cursor, nome, preco, quantidade):
        # Criar uma instância de Produto
        produto = Produto(nome, preco, quantidade)

        # Validar o produto
        resultado_validacao = produto.validar()
        if not resultado_validacao["status"]:
            return resultado_validacao

        # Inserir o produto no banco de dados
        cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (produto.nome, produto.preco, produto.quantidade))
        cursor.connection.commit()

        return {"status": True, "mensagem": resultado_validacao["mensagem"]}

    def verificar_estoque( cursor: Cursor):
        estoque = cursor.execute("""SELECT * FROM produtos""").fetchall()

        result = []
        for produto in estoque:
            result.append({"Codigo": produto[0], "Nome": produto[1], "Preco": produto[2], "Quantidade": produto[3]})

        return result
    
    def atualizar_produto(cursor: Cursor, codigo, nova_quantidade):
        produto = cursor.execute("SELECT * FROM produtos WHERE codigo = ?", (codigo,)).fetchone()

        if not produto:
            return {"status": False, "mensagem": "Produto não cadastrado!"}

        if nova_quantidade < 0:
            return {"status": False, "mensagem": "Quantidade inválida!"}
        
        cursor.execute("UPDATE produtos SET quantidade = ? WHERE codigo = ?", (nova_quantidade, codigo))
        cursor.connection.commit()    
        
        return {"status": False, "mensagem": "Quantidade atualizada!"}
