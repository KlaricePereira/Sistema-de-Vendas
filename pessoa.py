#A classe Pessoa é uma classe genérica que representa uma pessoa com algumas informações básicas, como o ID, nome e endereço. 
class Pessoa:
    def __init__(self, new_id, new_nome, new_endereco):
        self._id = new_id
        self._nome = new_nome
        self._endereco = new_endereco

#Método __str__ para retornar uma string com as informações.
    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, preco = {self._endereco}'

#Permite que esses valores sejam acessados e modificados por meio de métodos de acesso (getter) e métodos de modificação (setter).
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, new_nome):
        self._nome = new_nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, new_endereco):
        self._endereco = new_endereco
