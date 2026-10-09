# SLIDE 4 DO DOCS (POO.1)

pi = 3.14

class Circulo:
    def __init__(self):
        self.raio = 0
    def area_circulo(self):
        return pi * self.raio ** 2
    def circunferencia_circulo(self):
        return 2 * pi * self.raio


x = Circulo.raio()
x.raio = 5
print(f"O circulo que possui raio {x.raio}, possui a área {x.area_circulo()}")