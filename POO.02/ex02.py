class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.__distancia = distancia
        self.__horas = horas
        self.__minutos = minutos
    def set_distancia(self, ds):
        if ds > 0: self.__distancia = ds
        else: raise ValueError("A distância deve ser positiva.")
    def get_distancia(self):
        return self.__distancia
    def set_horas(self, h):
        if h >= 0: self.__horas = h
        else: raise ValueError
    def get_horas(self):
        return self.__horas
    def set_minutos(self, m):
        if m >= 0: self.__minutos = m
        else: raise ValueError
    def get_minutos(self):
        return self.__minutos
    def calcular_velocidade_media(self):
        tempo_total = self.__horas + (self.__minutos / 60)
        if tempo_total == 0:
            return 0
        return self.__distancia / tempo_total