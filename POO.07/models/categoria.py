# Categoria + CategoriaDAO

import json

class Categoria:
    def __init__(self, id: int, descricao: str):
        self.set_id(id)
        self.set_descricao(descricao)

    def get_id(self) -> int: 
        return self.__id
    def get_descricao(self) -> str: 
        return self.__descricao

    def set_id(self, id: int) -> None: 
        self.__id = id
    def set_descricao(self, descricao: str) -> None: 
        self.__descricao = descricao

    def __str__(self) -> str:
        return f"ID: {self.__id} | Descrição: {self.__descricao}"

    def to_json(self) -> dict:
        return {"id": self.__id, "descricao": self.__descricao}

    @staticmethod
    def from_json(dic: dict):
        return Categoria(dic["id"], dic["descricao"])


class CategoriaDAO:
    __objetos = []

    @classmethod
    def inserir(cls, obj: Categoria) -> None:
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
    def listar_id(cls, id: int) -> Categoria:
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj: Categoria) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj: Categoria) -> None:
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls) -> None:
        cls.__objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    cls.__objetos.append(Categoria.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls) -> None:
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Categoria.to_json, indent=4)