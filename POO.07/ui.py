from service import Service

class UI:
    @staticmethod
    def main() -> None:
        op = 0
        while op != 99:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            elif op == 2: UI.cliente_listar()
            elif op == 3: UI.cliente_atualizar()
            elif op == 4: UI.cliente_excluir()
            elif op == 5: UI.categoria_inserir()
            elif op == 6: UI.categoria_listar()
            elif op == 7: UI.categoria_atualizar()
            elif op == 8: UI.categoria_excluir()
            elif op == 9: UI.produto_inserir()
            elif op == 10: UI.produto_listar()
            elif op == 11: UI.produto_atualizar()
            elif op == 12: UI.produto_excluir()
            elif op == 13: UI.produto_reajustar()

    @staticmethod
    def menu() -> int:
        print("\n=== MENU ADMIN ===")
        print("Clientes:   1-Inserir | 2-Listar | 3-Atualizar | 4-Excluir")
        print("Categorias: 5-Inserir | 6-Listar | 7-Atualizar | 8-Excluir")
        print("Produtos:   9-Inserir | 10-Listar | 11-Atualizar | 12-Excluir | 13-Reajustar")
        print("99 - Sair")
        return int(input("Escolha uma opção: "))



    @staticmethod
    def cliente_inserir() -> None:
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        Service.cliente_inserir(nome, email, fone)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def cliente_listar() -> None:
        clientes = Service.cliente_listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(c)

    @staticmethod
    def cliente_atualizar() -> None:
        UI.cliente_listar()
        id = int(input("ID do cliente a atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo fone: ")
        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado com sucesso!")

    @staticmethod
    def cliente_excluir() -> None:
        UI.cliente_listar()
        id = int(input("ID do cliente a excluir: "))
        Service.cliente_excluir(id)
        print("Cliente excluído com sucesso!")



    @staticmethod
    def categoria_inserir() -> None:
        descricao = input("Descrição da categoria: ")
        Service.categoria_inserir(descricao)
        print("Categoria inserida com sucesso!")

    @staticmethod
    def categoria_listar() -> None:
        categorias = Service.categoria_listar()
        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada.")
        else:
            for c in categorias:
                print(c)

    @staticmethod
    def categoria_atualizar() -> None:
        UI.categoria_listar()
        id = int(input("ID da categoria a atualizar: "))
        descricao = input("Nova descrição: ")
        Service.categoria_atualizar(id, descricao)
        print("Categoria atualizada com sucesso!")

    @staticmethod
    def categoria_excluir() -> None:
        UI.categoria_listar()
        id = int(input("ID da categoria a excluir: "))
        Service.categoria_excluir(id)
        print("Categoria excluída com sucesso!")



    @staticmethod
    def produto_inserir() -> None:
        descricao = input("Descrição do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        UI.categoria_listar()
        idCategoria = int(input("ID da Categoria: "))
        Service.produto_inserir(descricao, preco, estoque, idCategoria)
        print("Produto inserido com sucesso!")

    @staticmethod
    def produto_listar() -> None:
        produtos = Service.produto_listar()
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(p)

    @staticmethod
    def produto_atualizar() -> None:
        UI.produto_listar()
        id = int(input("ID do produto a atualizar: "))
        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        UI.categoria_listar()
        idCategoria = int(input("Novo ID da Categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, idCategoria)
        print("Produto atualizado com sucesso!")

    @staticmethod
    def produto_excluir() -> None:
        UI.produto_listar()
        id = int(input("ID do produto a excluir: "))
        Service.produto_excluir(id)
        print("Produto excluído com sucesso!")

    @staticmethod
    def produto_reajustar() -> None:
        percentual = float(input("Percentual de reajuste (ex: 10 para +10% ou -10 para -10%): "))
        Service.produto_reajustar(percentual)
        print("Preços reajustados com sucesso!")

if __name__ == "__main__":
    UI.main()