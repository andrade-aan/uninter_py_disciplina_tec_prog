print('Bem-Vindo a Sorveteria ALEX DE ANDRADE NASCIMENTO')  # Apresentação do estabelecimento
print()
print('Opções Disponíveis em Nosso Cardápio para Você')  # Apresentação do Cardápio para a Escolha do Cliente
print()
print('° ' * 48)
print('| CÓDIGO |     DESCRIÇÃO        | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml) |')
print('|   TR   | Sabores Tradicionais |      R$ 6.00      |      R$ 10.00      |      R$ 18.00      |')
print('|   ES   | Sabores Especiais    |      R$ 7.00      |      R$ 12.00      |      R$ 21.00      |')
print('|   PR   | Sabores Premium      |      R$ 8.00      |      R$ 14.00      |      R$ 24.00      |')
print('° ' * 48)
print()

preco_tr_p = 6.00 #Criação das constantes de valor para os tamanhos P/M/G e sabores TR/ES/PR
preco_es_p = 7.00
preco_pr_p = 8.00
preco_tr_m = 10.00
preco_es_m = 12.00
preco_pr_m = 14.00
preco_tr_g = 18.00
preco_es_g = 21.00
preco_pr_g = 24.00

total_pedido = float() #Criação da variável de preço final a pagar

tamanho = '' #Criação vazia para variáveis
sabor = ''

#Repetição para a escolha do cliente e tratamento de possíveis erros de escolha
while True:
    simounao = ''#Criação da variável de parada ou repetição e atribuição nula para evitar erro na lógica de repetição
    while tamanho != 'P' and tamanho != 'M' and tamanho != 'G' and tamanho != 'p' and tamanho != 'm' and tamanho != 'g': #repetição para a escolha do tamanho
        tamanho = input('Por favor, escolha entre os tamanhos disponíveis conforme os códigos do nosso Cardápio (P/M/G): ')
        if tamanho != 'P' and tamanho != 'M' and tamanho != 'G' and tamanho != 'p' and tamanho != 'm' and tamanho != 'g':
            print('Poxa!!! Acho que você digitou uma opção inválida, isso acontece, tente novamente!!!')
    while sabor != 'TR' and sabor != 'tr' and sabor != 'ES' and sabor != 'es' and sabor != 'PR' and sabor != 'pr':#repetição para a escolha do sabor
        sabor = input('Agora escolha um dos nossos deliciosos sabores (TR/ES/PR): ')
        if sabor != 'TR' and sabor != 'tr' and sabor != 'ES' and sabor != 'es' and sabor != 'PR' and sabor != 'pr':
            print('Poxa!!! Acho que você digitou uma opção inválida, isso acontece, tente novamente!!!')
    if sabor == 'TR' or sabor == 'tr':#Cálculo do pedido para sabor TRadicional com P/M/G
        if tamanho == 'P' or tamanho == 'p':
            total_pedido += preco_tr_p
        elif tamanho == 'M' or tamanho == 'm':
            total_pedido += preco_tr_m
        else:
            total_pedido += preco_tr_g
    elif sabor == 'ES' or sabor == 'es':#Cálculo do pedido para sabor ESpecial com P/M/G
        if tamanho == 'P' or tamanho == 'p':
            total_pedido = total_pedido + (preco_es_p)
        elif tamanho == 'M' or tamanho == 'm':
            total_pedido += preco_es_m
        else:
            total_pedido += preco_es_g
    else:               #Cálculo do pedido para sabor PRemium com P/M/G
        if tamanho == 'P' or tamanho == 'p':
            total_pedido = total_pedido + (preco_pr_p)
        elif tamanho == 'M' or tamanho == 'm':
            total_pedido += preco_pr_m
        else:
            total_pedido += preco_pr_g
    if simounao != 'F' and simounao != 'C' and simounao != 'f' and simounao != 'c':#Solicitação de finalização do pedido ou continuidade.
        simounao = input('Quer (F)inalizar o pedido ou deseja (C)ontinuar? ')
        sabor = ''#Atibuição nula das variáveis para evitar duplicidade ao retornar para nova escolha
        tamanho = ''
    if simounao != 'C' and simounao != 'c' and simounao != 'F' and simounao != 'f':
        print('Ops!!! Opção Inválida!!! Com mais um erro de escolha vou entender que você quer finalizar o pedido!!!')
    if simounao == 'C' or simounao == 'c':
        continue #Volta ao início do while True
    simounao = input('Vamos tentar novamente. Quer (F)inalizar o pedido ou deseja (C)ontinuar? ')
    if simounao == 'C' or simounao == 'c':
        continue #Volta ao início do while True
    else: # Após dois erros seguidos ou a confirmação da opção (F)inalizar, o programa se encerra com a exibição do somatório da variável total_pedido
        print('O valor total do seu pedido é de R$ {:.2f}'.format(total_pedido))
        break