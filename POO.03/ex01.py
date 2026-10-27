class Triangulo:
    def __init__ (self, b, h):
        self.__base = b
        self.__altura = h
    def set_base(self, v):
        if v > 0: self.__base = v
        else: raise ValueError("Base deve ser positiva.")
    def get_base(self):
        return self.__base
    def set_altura(self, v):
        if v > 0: self.__altura = v
        else: raise ValueError("Altura deve ser positiva.")
    def get_altura(self):
        return self.__altura
    def calcular_area(self):
        return self.__base * self.__altura / 2
    def __str__(self):
        return f"Base: {self.__base} - Altura: {self.__altura}"
class UI:
    @staticmethod
    def main():
        x = Triangulo(20, 30)
        print(x.calcular_area())
        x.set_base(10)
        x.set_altura(20)
        print(x.calcular_area())

UI.main()