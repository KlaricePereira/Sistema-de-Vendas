#Essa é uma classe que define um produto com três atributos: id, nome e preço. Ela possui um construtor que recebe como parâmetros um id, um nome e um preço, e inicializa esses atributos.
class Produto:

    def __init__(self, new_id, new_nome, new_preco):
        self._id = new_id
        self._nome = new_nome
        self._preco = new_preco

#define um método str que retorna uma string contendo as informações do produto.
    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, preco = {self._preco}'

#define getters e setters para os três atributos, permitindo que eles possam ser lidos e modificados de fora da classe. Os getters retornam o valor dos atributos, enquanto os setters atualizam os valores dos atributos com novos valores passados como parâmetro.
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
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, new_preco):
        self._preco = new_preco
