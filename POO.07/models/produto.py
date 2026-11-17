# Produto + ProdutoDAO

import json

class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int, idCategoria: int):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)

    def get_id(self) -> int: 
        return self.__id
    def get_descricao(self) -> str: 
        return self.__descricao
    def get_preco(self) -> float: 
        return self.__preco
    def get_estoque(self) -> int: 
        return self.__estoque
    def get_idCategoria(self) -> int: 
        return self.__idCategoria

    def set_id(self, id: int) -> None: 
        self.__id = id
    def set_descricao(self, descricao: str) -> None: 
        elf.__descricao = descricao
    def set_preco(self, preco: float) -> None: 
        self.__preco = preco
    def set_estoque(self, estoque: int) -> None: 
        self.__estoque = estoque
    def set_idCategoria(self, idCategoria: int) -> None: 
        self.__idCategoria = idCategoria

    def __str__(self) -> str:
        return (f"ID: {self.__id} | Descrição: {self.__descricao} | "
                f"Preço: R$ {self.__preco:.2f} | Estoque: {self.__estoque} | "
                f"ID Categoria: {self.__idCategoria}")

    def to_json(self) -> dict:
        return {
            "id": self.__id,
            "descricao": self.__descricao,
            "preco": self.__preco,
            "estoque": self.__estoque,
            "idCategoria": self.__idCategoria
        }

    @staticmethod
    def from_json(dic: dict):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])


class ProdutoDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj: Produto) -> None:
        cls.abrir()
        id = 0
        for aux in cls.__objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id: int) -> Produto:
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Produto) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj: Produto) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls) -> None:
        cls.__objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    cls.__objetos.append(Produto.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Produto.to_json, indent=4)