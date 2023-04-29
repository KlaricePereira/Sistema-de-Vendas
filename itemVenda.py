#A classe ItemVenda representa um item de venda que contém informações sobre o produto vendido, a quantidade vendida e o desconto aplicado na venda desse item.
class ItemVenda:

#O construtor da classe recebe como parâmetros o objeto Produto vendido, a quantidade vendida e o desconto aplicado na venda desse item. 
    def __init__(self, new_produto, new_quantidade, new_desconto):
        self._produto = new_produto
        self._quantidade = new_quantidade
        self._desconto = new_desconto

#O método __str__ é uma representação em string do objeto ItemVenda, que exibe as informações sobre o produto vendido, a quantidade e o desconto aplicado.
    def __str__(self):
        return f'produto: {self._produto}, quantidade = {self._quantidade}, desconto = {self._desconto}'

#A classe possui getters e setters para acessar e modificar as informações do item.
    @property
    def produto(self):
        return self._produto

    @produto.setter
    def produto(self, new_produto):
        self._produto = new_produto

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, new_quantidade):
        self._quantidade = new_quantidade

    @property
    def desconto(self):
        return self._desconto

    @desconto.setter
    def desconto(self, new_desconto):
        self._desconto = new_desconto

#Os métodos get_valor_unitario e get_valor_total são responsáveis por calcular o valor unitário e total do item de venda, levando em consideração o preço do produto e o desconto aplicado na venda. O valor unitário é calculado como o preço do produto vezes o complemento da taxa de desconto em porcentagem. O valor total é calculado como a quantidade vendida vezes o valor unitário.
    def get_valor_unitario(self):
        return self._produto.preco * (1 - self._desconto / 100)

    def get_valor_total(self):
        return self._quantidade * self.get_valor_unitario()