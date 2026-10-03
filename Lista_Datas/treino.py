from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, dt: datetime, ds: float, t: timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t
    def get_id(self) -> int:
        return self.__id
    def get_data(self) -> datetime:
        self.__data = dt
    def get_distancia(self) -> float:
        return self.__distancia
    def get_tempo(self) -> timedelta:
        return self.__tempo
    def set_id(self, id: int):
        self.__id = id
    def set_data(self, dt: datetime):
        self.__data = 
    def set_distancia(self, ds: float):
        self.__distancia = ds
    def set_tempo(self, t: timedelta):
        self.__tempo = t

    def pace() -> timedelta:
        if self.__distancia <= 0:
            return timedelta(seconds = 0)
        segundos_totais = self.__tempo.total_seconds()
        segundos_por_km = segundos_totais / self.__distancia
        return timedelta(seconds = segundos_por_km)

    def __str__(self) -> str:
        data_formatada = self.__data.strftime("%d/%m/%Y")
        pace_total = self.pace()
        minutos = int(pace_total.total_seconds() // 60)
        segundos = int(pace_total.total_seconds() % 60)
        pace_str = f"{minutos:02d}:{segundos:02d} min/km"

        return (
            f"ID: {self.__id} | Data: {data_formatada} | "
            f"Distancia: {self.__distancia} km | Tempo: {self.__tempo} | "
            f"Pace: {pace_str}"
        )


class TreinoUI:
    __treinos = []
    @classmethod
    def Main(cls):
        opcao = -1
        while opcao !=  0:
            opcao = cls.Menu()

            if opcao == 1:
                cls.Inserir()
            elif opcao == 2:
                cls.Listar()
            elif opcao == 3:
                cls.Listar_Id()
            elif opcao == 4:
                cls.Atualizar()
            elif opcao == 5:
                cls.Excluir()
            elif opcao == 6:
                cls.MaisRapido()
            elif opcao == 0:
                print("\nAplicacao encerrada. Ate mais!")
            else:
                print("\nOpcao invalida! Tente novamente")
    
    @staticmethod
    def Menu() -> int:
        """Exibe o menu e retorna a opção escolhida pelo usuário."""
        print("\n================ MENU ================")
        print("1 - Inserir novo treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Treino mais rápido (menor pace)")
        print("0 - Sair")
        print("======================================")
        
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @classmethod
    def Inserir(cls):
        """Insere um novo treino na lista."""
        print("\n--- Inserir Treino ---")
        try:
            id_treino = int(input("ID do treino: "))
            for t in cls.__treinos:
                if t.get_id() == id_treino:
                    print("Erro: Já existe um treino com este ID!")
                    return

            data_str = input("Data (DD/MM/AAAA): ")
            dt = datetime.strptime(data_str, "%d/%m/%Y")
            
            distancia = float(input("Distância (km): "))
            
            minutos = int(input("Tempo gasto (minutos): "))
            segundos = int(input("Tempo gasto (segundos adicionais): "))
            tempo = timedelta(minutes = minutos, seconds = segundos)

            novo_treino = Treino(id_treino, dt, distancia, tempo)
            cls.__treinos.append(novo_treino)
            print("Treino inserido com sucesso!")
            
        except ValueError:
            print("Erro: Dados inseridos com formato inválido!")

    @classmethod
    def Listar(cls):
        """Lista todos os treinos cadastrados."""
        print("\n--- Lista de Treinos ---")
        if not cls.__treinos:
            print("Nenhum treino cadastrado.")
            return

        for t in cls.__treinos:
            print(t)

    @classmethod
    def Listar_Id(cls):
        """Busca e exibe um treino específico pelo seu ID."""
        print("\n--- Listar Treino por ID ---")
        try:
            id_busca = int(input("Informe o ID desejado: "))
            for t in cls.__treinos:
                if t.get_id() == id_busca:
                    print(t)
                    return
            print("Treino não encontrado com o ID informado.")
        except ValueError:
            print("Erro: Digite um ID numérico válido!")

    @classmethod
    def Atualizar(cls):
        """Atualiza os dados de um treino existente."""
        print("\n--- Atualizar Treino ---")
        try:
            id_busca = int(input("Informe o ID do treino a ser atualizado: "))
            for t in cls.__treinos:
                if t.get_id() == id_busca:
                    data_str = input("Nova Data (DD/MM/AAAA): ")
                    dt = datetime.strptime(data_str, "%d/%m/%Y")
                    
                    distancia = float(input("Nova Distância (km): "))
                    
                    minutos = int(input("Novo Tempo (minutos): "))
                    segundos = int(input("Novo Tempo (segundos adicionais): "))
                    tempo = timedelta(minutes=minutos, seconds=segundos)

                    t.set_data(dt)
                    t.set_distancia(distancia)
                    t.set_tempo(tempo)
                    
                    print("Treino atualizado com sucesso!")
                    return
                    
            print("Treino não encontrado com o ID informado.")
        except ValueError:
            print("Erro: Entrada de dados inválida!")

    @classmethod
    def Excluir(cls):
        """Exclui um treino da lista a partir do seu ID."""
        print("\n--- Excluir Treino ---")
        try:
            id_busca = int(input("Informe o ID do treino a excluir: "))
            for t in cls.__treinos:
                if t.get_id() == id_busca:
                    cls.__treinos.remove(t)
                    print("Treino excluído com sucesso!")
                    return
            print("Treino não encontrado com o ID informado.")
        except ValueError:
            print("Erro: Digite um ID numérico válido!")

    @classmethod
    def MaisRapido(cls):
        """Encontra e mostra o treino com o menor pace (maior velocidade)."""
        print("\n--- Treino Mais Rápido ---")
        if not cls.__treinos:
            print("Nenhum treino cadastrado.")
            return

        
        mais_rapido = min(cls.__treinos, key=lambda t: t.pace())
        print(mais_rapido)

if __name__ == "__main__":
    TreinoUI.Main()