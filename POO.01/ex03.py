"""
Uma Conta Bancária
A classe deve ter atributos para armazenar o nome do titular da conta, o número da conta e o saldo e métodos para
realizar as operações de depositar um valor, sacar um valor e verificar o saldo atual.
Escrever um programa para testar a classe.
"""

class ContaBancaria:
    def __init__ (self, titular, numero_conta, saldo_atual):
        self.titular = titular
        self.conta = numero_conta
        self.saldo = saldo_atual
    def depositar_valor(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
        else:
            print("Apenas valores positivos podem ser depositados")
    def sacar_valor(self, valor):
        if valor <= self.saldo
            self.saldo = self.saldo - valor
        else:
            print("Saldo insuficiente. Saque indisponível!")
    def verificar_saldo(self):
        return self.saldo

# Teste da Classe:
minha_conta = ContaBancaria("Bruno", 123456789, 250.00)
print(minha_conta)
minha_conta.depositar_valor(3.00)
print(minha_conta)