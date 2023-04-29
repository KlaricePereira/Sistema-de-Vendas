#Esse código apresenta uma classe Cliente que herda da classe Pessoa. 
from pessoa import Pessoa


class Cliente(Pessoa):

#A classe Cliente possui atributos específicos, como cartao_fidelidade e pontos. O construtor da classe recebe como parâmetros um id, um nome, um endereco, um cartao_fidelidade e um pontos, que são usados para inicializar os atributos correspondentes.
    def __init__(self, new_id, new_nome, new_endereco, new_cartao_fidelidade, new_pontos):
        super().__init__(new_id, new_nome, new_endereco)
        self._cartao_fidelidade = new_cartao_fidelidade
        self._pontos = new_pontos

#O método __str__ retorna uma representação em string do objeto, exibindo os valores dos atributos.
    def __str__(self):
        return f'id = {self._id}, nome = {self._nome}, endereco = {self._endereco}, ' \
               f'cartao_fidelidade = {self._cartao_fidelidade}, pontos = {self._pontos}'

#A classe possui dois métodos @property e seus respectivos @<propriedade>.setter, que são usados para encapsular o acesso aos atributos cartao_fidelidade e pontos. Dessa forma, é possível controlar o acesso e alteração dos valores desses atributos de forma mais segura e consistente.
    @property
    def cartao_fidelidade(self):
        return self._cartao_fidelidade

    @cartao_fidelidade.setter
    def cartao_fidelidade(self, new_cartao_fidelidade):
        self._cartao_fidelidade = new_cartao_fidelidade

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, new_pontos):
        self._pontos = new_pontos
