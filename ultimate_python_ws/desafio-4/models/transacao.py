from .produto import Produto
from sqlite3 import Cursor

class Transacao():
    def __init__(self, codigo_produto, quantidade, id=None):
        self.id = id
        self.codigo_produto = codigo_produto
        self.quantidade = quantidade

    def comprar(cursor: Cursor, nome, quantidade):
        produto_em_carrinho = cursor.execute("""SELECT * FROM produtos WHERE nome = ?""", (nome,)).fetchone()
        if not produto_em_carrinho:
            return {"status": False, "mensagem": "Produto indisponível!"}

        produto = Produto(codigo=produto_em_carrinho[0],
                          nome=produto_em_carrinho[1],
                          preco=produto_em_carrinho[2],
                          quantidade=produto_em_carrinho[3],
                          )

        if produto.quantidade < quantidade:
            return {"status": False, "mensagem": "Quantidade indisponível!"}
        
        nova_quantidade = produto.quantidade - quantidade
        efetivando_compra = cursor.execute("""UPDATE produtos SET quantidade = ? WHERE codigo = ?""", (nova_quantidade, produto.codigo))
        venda = Transacao(produto.codigo, quantidade)

        salvando_compra = cursor.execute("""INSERT INTO vendas (codigo_produto, quantidade) VALUES (?, ?)""", (venda.codigo_produto, venda.quantidade))

        cursor.connection.commit()

        return {"status": True, "mensagem": "Produto comprado!", "produto": produto, "nova_quantidade": nova_quantidade}

    def relatorio(cursor: Cursor):
        vendas = cursor.execute("""SELECT * FROM vendas""").fetchall()

        total = 0
        for venda in vendas:
            preco_produto = cursor.execute("SELECT preco FROM produtos WHERE codigo = ?", (int(venda[1]),)).fetchone()
            total += preco_produto[0]

        return {"total": total, "vendas": vendas}