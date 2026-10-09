"""
Uma Viagem
A classe deve ter atributos para armazenar a distância percorrida na viagem em km e o tempo gasto em horas e
minutos. A classe deve possuir método para calcular a velocidade média atingida na viagem em km/h de acordo
com a distância e o tempo gasto.
Escrever um programa para testar a classe.
"""

class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.horas = horas
        self.minutos = minutos
    def calcular_velocidade_media(self):
        tempo_total = self.horas + (self.minutos / 60)
        if tempo_total == 0:
            return 0
        return self.distancia / tempo_total

# Programa de teste:
