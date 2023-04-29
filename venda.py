from itemVenda import ItemVenda

#A classe Venda tem um construtor __init__ que recebe um argumento new_cliente e armazena-o em uma variável de instância chamada _cliente. Além disso, também inicializa uma lista vazia de itens de venda chamada _itens.
class Venda:
    def __init__(self, new_cliente):
        self._cliente = new_cliente
        self._itens = []

#inclui_item(self, item_venda: ItemVenda): Este método recebe um objeto ItemVenda como argumento e adiciona-o à lista _itens. Antes de adicionar o item, ele verifica se já existe um item com o mesmo produto na lista, incrementando a quantidade em vez de adicionar um novo item.
    def inclui_item(self, item_venda: ItemVenda):
        for item in self._itens:
            if item_venda.produto == item.produto:
              item_venda.quantidade += 1
        self._itens.append(item_venda)

#get_total(self): Este método calcula e retorna o valor total da venda somando o valor unitário de todos os itens na lista _itens.
    def get_total(self):
        total = 0
        for item in self._itens:
            total += item.get_valor_unitario()
        return total

#get_produto_mais_vendido(self): Este método retorna o item de venda mais vendido, ou seja, aquele com a maior quantidade na lista _itens.
    def get_produto_mais_vendido(self):
        mais_vendido = self._itens[0]
        for item in self._itens:
            if item.quantidade > mais_vendido.quantidade:
                mais_vendido = item
        return mais_vendido

#A classe Venda redefine o método __str__ para retornar uma string que representa a venda, incluindo o nome do cliente, a lista de produtos e o valor total da venda.
    def __str__(self):
        result = f'Cliente: {self._cliente.nome} - Produtos: '
        for item in self._itens:
            result += f'{item.produto.nome},  '
        result += f'Total = {self.get_total()}'
        return result