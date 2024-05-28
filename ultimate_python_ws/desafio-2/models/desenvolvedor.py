from .funcionario import Funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, endereco, tipoDeContrato, salario_base, linguagens):
        super().__init__(nome, idade, endereco, tipoDeContrato ,salario_base)
        
        self.validar_linguagens(linguagens)
        
        self.linguagens = linguagens
    
    def validar_linguagens(self, linguagens):
        if not isinstance(linguagens, str):
            raise ValueError("As linguagens devem ser um texto separado por virgulas!")
    
    def calcular_pagamento(self, num_projetos=0):
        bonus = num_projetos * 1000  
        return self.salario_base + bonus
