from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO

class Service:
    @staticmethod
    def cliente_inserir(nome: str, email: str, fone: str) -> None:
        c = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(c)

    @staticmethod
    def cliente_listar() -> list:
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id: int) -> Cliente:
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id: int, nome: str, email: str, fone: str) -> None:
        c = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(c)

    @staticmethod
    def cliente_excluir(id: int) -> None:
        c = Cliente(id, "", "", "")
        ClienteDAO.excluir(c)



    @staticmethod
    def categoria_inserir(descricao: str) -> None:
        c = Categoria(0, descricao)
        CategoriaDAO.inserir(c)

    @staticmethod
    def categoria_listar() -> list:
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id: int) -> Categoria:
        return CategoriaDAO.listar_id(id)

    @staticmethod
    def categoria_atualizar(id: int, descricao: str) -> None:
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)

    @staticmethod
    def categoria_excluir(id: int) -> None:
        c = Categoria(id, "")
        CategoriaDAO.excluir(c)



    @staticmethod
    def produto_inserir(descricao: str, preco: float, estoque: int, idCategoria: int) -> None:
        p = Produto(0, descricao, preco, estoque, idCategoria)
        ProdutoDAO.inserir(p)

    @staticmethod
    def produto_listar() -> list:
        return ProdutoDAO.listar()

    @staticmethod
    def produto_listar_id(id: int) -> Produto:
        return ProdutoDAO.listar_id(id)

    @staticmethod
    def produto_atualizar(id: int, descricao: str, preco: float, estoque: int, idCategoria: int) -> None:
        p = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(p)

    @staticmethod
    def produto_excluir(id: int) -> None:
        p = Produto(id, "", 0.0, 0, 0)
        ProdutoDAO.excluir(p)

    @staticmethod
    def produto_reajustar(percentual: float) -> None:
        produtos = ProdutoDAO.listar()
        for p in produtos:
            novo_preco = p.get_preco() * (1 + percentual / 100)
            p.set_preco(novo_preco)
            ProdutoDAO.atualizar(p)