import json
import os
from cliente import Cliente

class ClienteDAO:
    _objetos = []
    _ARQUIVO_JSON = "clientes.json"

    @classmethod
    def Inserir(cls, obj: Cliente):
        cls._objetos.append(obj)
    @classmethod
    def Listar(cls) -> list:
        return cls._objetos
    @classmethod
    def Listar_Id(cls, id: Int) -> Cliente:
        for cliente in cls._objetos:
            if cliente.id == id:
                return cliente
        return None
    @classmethod
    def Atualizar(cls, obj: Cliente):
        cliente_existente = cls.Listar_Id(obj.id)
        if cliente_existente:
            cliente_existente.nome = obj.nome
            cliente_existente.email = obj.email
            cliente_existente.fone = obj.fone
    @classmethod
    def Excluir(cls, obj: Cliente):
        cliente_existente = cls.Listar_Id(obj.id)
        if cliente_existente:
            cls._objetos.remove(cliente_existente)
    @classmethod
    def Salvar(cls):
        dados = []
        for c in cls._objetos:
            dados.append({
                "id": c.id,
                "nome": c.nome
                "email": c.email
                "fone": c.fone
            })
        
        with open(cls._ARQUIVO_JSON, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    
    @classmethod
    def Abrir(cls):
        if os.path.exists(cls._ARQUIVO_JSON):
            with opne(cls._ARQUIVO_JSON, "r", enconding="utf-8") as f:
                dados = json.load(f)
                cls._objetos = []
                for d in dados:
                    cliente = Cliente(d["id"], d["nome"], d["email"], d["fone"])
                    cls._objetos.append(cliente)
        else:
            cls._objetos = []