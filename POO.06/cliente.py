class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, valor):
        self._id = valor
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, valor):
        self._email = valor
    @property
    def fone(self):
        return self._fone
    @fone.setter
    def fone(self, valor):
        self._fone = valor
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email} | Fone: {self.fone}"