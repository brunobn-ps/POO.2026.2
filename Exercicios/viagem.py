class Viagem:
    def __init__(self, destino, distancia, litros):
        self.set_destino(destino)
        self.set_distancia(distancia)
        self.set_litros(litros)
    def set_destino(self, nome):
        if isinstance(nome, str): self.__destino = nome
        else: raise ValueError("O destino precisa ser uma palavra/um texto.")
    def set_distancia(self, valor):
        if valor > 0: self.__distancia = valor
        else: raise ValueError("Distância percorrida deve ser positiva.")
    def set_litros(self, lt):
        if lt > 0: self.__litros = lt
        else: raise ValueError("Litragem utilizada deve ser positiva.")
    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    def consumo(self):
        return self.__distancia / self.__litros
    def ToString(self):
        return f"Destino da Viagem: {self.__destino} --- Distância da Viagem: {self.__distancia} --- Litros consumidos: {self.__litros}"
    def __str__(self):
        return self.ToString()


class ViagemUI:
    @staticmethod
    def menu():
        print("---MENU\n---")
        print("1 - Calcular o Consumo da Viagem")
        print("2 - Fim do Programa")
        opcao = int(input("Digite a opção desejada: "))
        return opcao

    @staticmethod
    def calculo():
        print("\n---CADASTRO DA VIAGEM---")
        destino = input("Informe o destino da sua viagem: ")
        distancia = float(input("Informe a distância percorrida(km): "))
        litros = float(input("Por último, informe a quantidade de combustível gasta(litros): "))

        v1 = Viagem(destino, distancia, litros)

        print("\n---DADOS DA VIAGEM---")
        print(v1.ToString())
        print(f"Consumo médio: {v1.consumo():.2f} km/l")
    
    @staticmethod
    def main():
        op = ViagemUI.menu()
        while op != 2:
            if op == 1:
                try:
                    ViagemUI.calculo()
                except ValueError as e:
                    print(f"Erro ao cadastrar viagem: {e}")
            else:
                print("Opção inválida! Tente novamente.")
            
            op = ViagemUI.menu()
        print("Programa finalizado.")

if __name__ == "__main__":
    ViagemUI.main()