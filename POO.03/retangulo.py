import math

class Retangulo:
    def __init__ (self, b, h):
        self.__base = b
        self.__altura = h
    def set_base(self, v):
        if v > 0: self.__base = v
        else: raise ValueError("Base deve ser positiva.")
    def set_altura(self, v):
        if v > 0: self.__altura = v
        else: raise ValueError("Altura deve ser positiva.")
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura
    def area_retangulo(self):
        return self.__base * self.__altura
    def diag_retangulo(self):
        return math.sqrt(self.__base ** 2 + self.__altura ** 2)
    def ToString(self):
        return f"Base do Retângulo: {self.__base} --- Altura do Retângulo: {self.__altura}"
    def __str__(self):
        return self.ToString()

class UI:
    @staticmethod
    def main():
        r1 = Retangulo(20, 20)
        print(f"Área: {r1.area_retangulo()}")
        r1.set_base(10)
        r1.set_altura(5)
        print(f"ToString: {r1.ToString()}")
        print(f"Diagonal: {r1.diag_retangulo():.2f}")

UI.main()