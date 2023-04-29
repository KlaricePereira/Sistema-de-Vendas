#importa as classes que serão usadas
from produto import Produto
from cliente import Cliente
from itemVenda import ItemVenda
from venda import Venda

#O código apresentado usa a construção "if name == 'main':" para verificar se o módulo está sendo executado como um programa principal ou se está sendo importado como um módulo em outro programa.
if __name__ == '__main__':

#Cria três objetos Produto, que representam diferentes produtos que serão vendidos. 
    feijao = Produto(1, 'Feijão', 20)
    arroz = Produto(2, 'Arroz', 15)
    farinha = Produto(3, 'Farinha', 10)

#Cria três objetos ItemVenda, que representam as vendas individuais de cada produto, com suas respectivas quantidades e descontos.
    iv_feijao = ItemVenda(feijao, 2, 1)
    iv_arroz = ItemVenda(arroz, 1, 0)
    iv_farinha = ItemVenda(farinha, 1, 0)
  
#Um objeto Cliente é criado, que representa o comprador da venda. 
    joao = Cliente(1, 'João', 'São Paulo', 'Dotz', 200)

#O objeto Venda é criado, passando o objeto Cliente como parâmetro.
    venda = Venda(joao)

#O código adiciona os objetos ItemVenda à Venda usando o método inclui_item(), que calcula o preço total da venda e armazena o produto mais vendido.
    venda.inclui_item(iv_feijao)
    venda.inclui_item(iv_arroz)
    venda.inclui_item(iv_arroz)
    venda.inclui_item(iv_arroz)
    venda.inclui_item(iv_farinha)

#Por fim, o código imprime o total da venda, o produto mais vendido e uma representação em string da venda.
    print(venda.get_total())
    print(venda.get_produto_mais_vendido())
    print(venda)
  
