from models.desenvolvedor import Desenvolvedor
from models.gerente import Gerente
from lib.database import Database


def create_app():
    db = Database("funcionarios.db")
    
    db.execute_query("""CREATE TABLE IF NOT EXISTS desenvolvedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL,
            endereco VARCHAR(255) NOT NULL,
            tipoDeContrato VARCHAR(10) NOT NULL,
            salario FLOAT NOT NULL,
            linguagens TEXT NOT NULL
        );""")

    db.execute_query("""CREATE TABLE IF NOT EXISTS gerentes (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome VARCHAR(255) NOT NULL,
            idade INT NOT NULL,
            endereco VARCHAR(255),
            tipoDeContrato VARCHAR(10) NOT NULL,
            salario FLOAT NOT NULL NOT NULL,
            bonus FLOAT NOT NULL
        );""")
    
    while(True):
        print("-------- Qual funcionário você deseja cadastrar? --------")
        print("[1] Desenvolvedor")
        print("[2] Gerente")
        print("[3] Sair do sistema")
        funcionario = int(input("Digite um número: "))    

        match(funcionario):
            case 1:
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                endereco = input("Endereço: ")
                tipoDeContrato = input("Tipo de Contrato (CLT/PJ): ")
                salario_base = float(input("Salário Base: "))
                linguagens = input("Linguagens (separadas por vírgula): ")
                projetos = int(input("Quantidade de projetos em atuação: "))

                try:
                    desenvolvedor = Desenvolvedor(nome, idade, endereco, tipoDeContrato, salario_base, linguagens)
                
                    db.execute_query("""INSERT INTO desenvolvedores (nome, idade, endereco, tipoDeContrato, salario, linguagens)
                        VALUES (?, ?, ?, ?, ?, ?);
                        """, (desenvolvedor.nome, 
                            desenvolvedor.idade, 
                            desenvolvedor.endereco, 
                            desenvolvedor.tipoDeContrato, 
                            desenvolvedor.calcular_pagamento(num_projetos=projetos), 
                            desenvolvedor.linguagens))
                    
                    db.connection.commit()
                    db.connection.close()
                    print("Desenvolvedor inserido com sucesso!")
                except ValueError as error:
                    print(error.args[0])
                    continue
                return
            
            case 2:
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                endereco = input("Endereço: ")
                tipoDeContrato = input("Tipo de Contrato (CLT/PJ): ")
                salario_base = float(input("Salário Base: "))
                vendas = float(input("Quantidade vendida: "))
                bonus = float(input("Bônus: "))
    
                try:
                    gerente = Gerente(nome, idade, endereco, tipoDeContrato, salario_base, bonus)
                   
                    db.execute_query("""
                        INSERT INTO gerentes (nome, idade, endereco, tipoDeContrato, salario, bonus)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (gerente.nome, gerente.idade, gerente.endereco, gerente.tipoDeContrato, gerente.calcular_pagamento(vendas), gerente.bonus))
                    
                    db.connection.commit()
                    db.connection.close()
                    print("Gerente inserido com sucesso!")
                except ValueError as e:
                    print("Erro ao criar gerente:", e)
                    return
            case 3:
                break
            case _:
                print("Cargo não existente na instituição!")

if __name__ == "__main__":  
    create_app()

"""
Marcio
21
Rasd
CLT
1000.00
Python,SQL
"""
"""
Gustavo
30
Rua dos Gerentes
PJ
5000.00
30000.00
200.0
"""