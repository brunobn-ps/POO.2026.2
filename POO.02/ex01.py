import math

class Circulo:
    def __init__ (self):
        self.__raio = 0
    def set_raio(self, v):
        self.__raio = v
    def get_raio(self):
        return self.__raio
    def area(self):
        return math.pi * (self.__raio ** 2)
    def circunferencia(self):
        return 2 * math.pi * self.__raio

x = Circulo()
x.set_raio(5)
print(f"O circulo que possui raio {x.get_raio()}, tem área equivalente a {x.area():.2f}")
print(f"e a circunferência {x.circunferencia():.2f}")