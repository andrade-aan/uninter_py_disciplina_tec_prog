print('Bem vindo ao ATACADÃO ALEX DE ANDRADE NASCIMENTO')# Apresentação do empreendimento
preco_unitario = float(input('Entre com o valor(R$) unitário do produto: '))# Definição e atribuição da variável do preço unitário
quantidade_produto = int(input('Entre com a quantidade de produtos para o cálculo do frete: '))# Definição/atribuição da variavel quantidade do produto
valor_frete = 30.00
if 0 <= quantidade_produto < 11:#Intervalo de valores para frete de até 10 unidades
    print('O valor da compra sem frete é de R$ {:.2f}'.format(preco_unitario*quantidade_produto))
    print('Valor do frete para {} unidades é de R$ {}'.format(quantidade_produto,valor_frete))
    print('O valor da compra com frete é de R$ {:.2f}'.format((preco_unitario*quantidade_produto)+valor_frete))
elif 11 <= quantidade_produto < 101:#Intervalo de valores para frete entre 11 até 100 unidades
    print('O valor da compra sem frete é de R$ {:.2f}'.format(preco_unitario*quantidade_produto))
    print('O valor do frete para {} unidades é de R$ {:.2f}'.format(quantidade_produto,valor_frete*2))
    print('O valor da compra com frete é de R$ {:.2f}'.format((valor_frete*2)+(preco_unitario*quantidade_produto)))
elif 101 <= quantidade_produto < 1001:#Intervalo de valores para frete entre 101 até 1000 unidades
    print('O valor da compra sem frete é de R$ {:.2f}'.format(quantidade_produto*preco_unitario))
    print('Valor do frete para {} unidades é de R$ {:.2f}'.format(quantidade_produto,valor_frete*4))
    print('O valor da compra com frete é de R$ {:.2f}'.format((valor_frete*4)+(quantidade_produto*preco_unitario)))
else:#Intervalo de valores para frete acima de 1000 unidades
    print('O valor da compra sem frete é de R$ {:.2f}'.format(quantidade_produto*preco_unitario))
    print('Valor do frete para {} unidades é de R$ {:.2f}'.format(quantidade_produto,valor_frete*8))
    print('O valor da compra com frete é de R$ {:.2f}'.format((valor_frete*8)+(quantidade_produto*preco_unitario)))