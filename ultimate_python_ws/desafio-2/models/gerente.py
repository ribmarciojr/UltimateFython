from .funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, idade, endereco, tipoDeContrato, salario_base, bonus):
        super().__init__(nome, idade, endereco, tipoDeContrato, salario_base)
        self.validar_bonus(bonus)
        self.bonus = bonus
        
    def validar_bonus(self, bonus):
        if not isinstance(bonus, (int, float)) or bonus < 0:
            raise ValueError("O bônus deve ser um número positivo.")
    
    def calcular_pagamento(self, vendas):
        comissao =  vendas * 0.05
        return self.salario_base + comissao + self.bonus
    