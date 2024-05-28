class Funcionario:
    def __init__(self, nome, idade, endereco, tipoDeContrato, salario):
        self.validar_nome(nome)
        self.validar_idade(idade)
        self.validar_endereco(endereco)
        self.validar_tipo_contrato(tipoDeContrato)
        self.validar_salario(salario)
        
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.tipoDeContrato = tipoDeContrato
        self.salario_base = salario
    
    def validar_nome(self, nome):
        if not isinstance(nome, str) or len(nome.strip()) == 0:
            raise ValueError("Nome inválido.")
    
    def validar_idade(self, idade):
        if not isinstance(idade, int) or idade <= 0:
            raise ValueError("Idade inválida.")
    
    def validar_endereco(self, endereco):
        if not isinstance(endereco, str) or len(endereco.strip()) == 0:
            raise ValueError("Endereço inválido.")
    
    def validar_tipo_contrato(self, tipoDeContrato):
        if tipoDeContrato not in ["CLT", "PJ"]:
            raise ValueError("Tipo de contrato inválido. Use 'CLT' ou 'PJ'.")
    
    def validar_salario(self, salario):
        if not isinstance(salario, (int, float)) or salario < 0:
            raise ValueError("Salário inválido.")
    
    def calcular_pagamento(self):
        return self.salario_base

