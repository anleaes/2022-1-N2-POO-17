from mailbox import NotEmptyError


class Pessoa:
    
    def _init_(self, nome, idade, endereco, telefone, email):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._telefone = telefone
        self._email = email