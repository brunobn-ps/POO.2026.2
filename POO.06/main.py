# QUESTÃO 2 DA LISTA 06

from cliente import Cliente
from cliente_dao import ClienteDAO

class UI:
    @staticmethod
    def Main():
        ClienteDAO.Abrir()
        op = -1
        while op != 0:
            op = UI.Menu()
            if op == 1:
                UI.Cliente_Listar()
            elif op == 2:
                UI.Cliente_Inserir()
            elif op == 3:
                UI.Cliente_Atualizar()
            elif op == 4:
                UI.Cliente_Excluir()
        ClienteDAO.Salvar()
    @staticmethod
    def Menu() -> int:
        print("\n--- MENU CLIENTES ---")
        print("1 - Listar")
        print("2 - Inserir")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    @staticmethod
    def Cliente_Listar():
        clientes = ClienteDAO.Listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(c)
    @staticmethod
    def Cliente_Inserir():
        id = int(input("Informe o ID: "))
        nome = input("Informe o Nome: ")
        email = input("Informe o Email: ")
        fone = input("Informe o Telefone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO.Inserir(c)
        print("Cliente inserido com sucesso!")
    @staticmethod
    def Cliente_Atualizar():
        id = int(input("Informe o ID do cliente a atualizar: "))
        c = ClienteDAO.Listar_Id(id)
        if c is None:
            print("Cliente não encontrado.")
        else:
            nome = input(f"Novo Nome ({c.nome}): ")
            email = input(f"Novo Email ({c.email}): ")
            fone = input(f"Novo Telefone ({c.fone}): ")
            novo_c = Cliente(id, nome, email, fone)
            ClienteDAO.Atualizar(novo_c)
            print("Cliente atualizado com sucesso!")
    @staticmethod
    def Cliente_Excluir():
        id = int(input("Informe o ID do cliente a excluir: "))
        c = ClienteDAO.Listar_Id(id)
        if c is None:
            print("Cliente não encontrado.")
        else:
            ClienteDAO.Excluir(c)
            print("Cliente excluído com sucesso!")

if __name__ == "__main__":
    UI.Main()