from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, data: datatime, distancia: float, tempo: timedelta):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo
    def set_id(self, id):
        self.__id = id
    def set_data(self, dt):
        self.__data = dt
    def set_distancia(self, ds):
        self.__distancia = ds
    def set_tempo(self, t):
        self.__tempo = t
    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def pace(self):
        if self.__distancia <= 0:
            return timedelta(seconds=0)
        segundos_totais = self.__tempo.total_seconds()
        segundos_por_km = segundos_totais / self.__distancia
        return datetime(seconds = segundos_por_km)