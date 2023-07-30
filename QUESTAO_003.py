# Identificação Empresa de Limpeza Alex de Andrade Nascimento

# Cálculo do valor total=(metragem*tipo)+adional(is)

"""
MENU CÁLCULO DO SERVIÇO BASEADO NA METRAGEM DO IMÓVEL

Argumentos para progressão no cálculo do valor com base na METRAGEM em m²

    de 30 a 299 -> R$60.00 + 30% da metragem -> custo_metragem = 60+(metragem_cliente*0.3)
    de 300 a 699 -> R$120.00 + 50% da metragem - > custo_metragem = 120+(metragem_cliente*0.5)

    de 29m² para baixo e de 700m² para cima não são aceitos serviços

"""
# Criação da função de borda
def borda(menu):
    """
        :parameter colocar o texto desejado para aplicação da borda,
        exemplo: borda('Digite o texto para aplicação da borda')
        :return     * ************************************** *
                    * Digite o texto para aplicação da borda *
                    * ************************************** *
    """
    tam = len(menu)
    if tam:
        print('*','*'*tam,'*')
        print('*',menu,'*')
        print('*','*'*tam,'*')

# Criação da Função metragem_limpeza()
def metragem_limpeza():
    print()
    borda('Cálculo do Serviço -- Custo da Limpeza por m²')
    print()
    while True:
        try:
            metragem_cliente = float(input('Informe a área em m² no qual o serviço de limpeza será executado:\n' + '>> '))
            if 30 <= metragem_cliente < 300: # Intervalo entre 30m² e 299.9m²
                custo_metragem = 60 + (metragem_cliente*0.3)
                return custo_metragem # Valor de retorno ao Programa
            elif 300 <= metragem_cliente < 700:# Intervalo entre 300m² e 699.9m²
                custo_metragem = 120 + (metragem_cliente * 0.5)
                return custo_metragem # Valor de retorno ao Programa
            else: # Tratamento para erro de digitação no caso de dado string
                print('Lamentamos, não aceitamos serviços em áreas menores de 30m² ou de 700m² ou mais!')
                continue
        except ValueError:
            print('Erro de entrada de dados!!')
"""
MENU TIPO DE LIMPEZA SOBRE CUSTO

Argumento para composição do valor do serviço baseado no tipo de limpeza a ser realizado

    B - BÁSICA -> sem adicional sobre o custo_metragem ou utilizar multiplicador 1.00 -> custo_metragem*fator_basico
    C - COMPLETA -> adicional de 30% sobre o custo_metragem, multiplicador 1.30 -> custo_metragem*fator_completo

"""
# Criação da Função tipo_limpeza()
def tipo_limpeza():
    print()
    borda('Cálculo do Serviço -- Custo da Limpeza por Mão-de-Obra Alocada')
    print()
    print('( B ) - Limpeza do tipo BÁSICA: indicada para limpezas rotineiras e sem uso de produtos especiais!')
    print('( C ) - Limpeza do tipo COMPLETA: indicada para limpezas pesadas e com uso de produtos especiais!')
    print()
    while True:
        escolha_limpeza = input('Escolha uma das opções para o Tipo de Limpeza (B ou C): \n' + '>> ')
        escolha_limpeza = escolha_limpeza.upper() #tratamento para digitação em minúsculo
        escolha_limpeza = escolha_limpeza.strip() #tratamento para digitação com espaço em branco
        if escolha_limpeza == 'B':
            custo_limpeza = (custo_metragem*1)-custo_metragem # Como o adicional de multiplicador é 1, não há adicional de valor
            return custo_limpeza
        elif escolha_limpeza == 'C':
            custo_limpeza = custo_metragem*0.3
            return custo_limpeza
        else:
            print('Você tem que escolher entre as opções ( B ) ou ( C )!')
            continue
"""
MENU SERVIÇOS ADICIONAIS

    0- Não desejo mais nada (encerrar)
    1- Passar 10 peças de roupas            R$ 10.00  adicional de 10.00 ao custo
    2- Limpeza de 1 Forno/Micro-ondas       R$ 12,00  adicional de 12.00 ao custo
    3- Limpeza de 1 Geladeira/Freezer       R$ 20,00  adicional de 20.00 ao custo

"""

# Criação da Função adicional_limpeza()
def adicional_limpeza():
    print()
    borda('Serviços Adicionais')
    print() # apresentação do Menu ao Usuário
    print('0- Não desejo mais nada (encerrar)\n' +
          '1- Passar 10 peças de roupas por R$ 10.00!\n' +
          '2- Limpeza de 1 Forno/Micro-ondas por R$ 12.00\n' +
          '3- Limpeza de 1 Geladeira/Freezer por R$ 20,00\n')
    contador_escolha = 0 # criação/atribuição da variável de somatório dos serviços adicionais
    while True:
        escolha_adicional = input('Deseja incluir mais alguns de nossos serviços adicionais?\n' + '>> ')
        if escolha_adicional == '0': # retorno do valor do adicional ao final do pedido, R$0.00 caso saída seja imediata
            return contador_escolha
        elif escolha_adicional == '1': # soma o valor ao serviço adicional escolhido
            contador_escolha += 10
            continue
        elif escolha_adicional == '2': # soma o valor ao serviço adicional escolhido
            contador_escolha += 12
            continue
        elif escolha_adicional == '3': # soma o valor ao serviço adicional escolhido
            contador_escolha += 20
            continue
        else: # caso haja digitação de valor fora das opções apresentadas
            print('Opção inválida! Escolha uma das opções listadas entre 0 a 3!')
            continue

# Início do Programa

borda('Bem-Vindo ao Programa LimpeTudo Alex de Andrade Nascimento')
print()
custo_metragem = metragem_limpeza()
custo_limpeza = tipo_limpeza()
contador_escolha = adicional_limpeza()
borda('Relatório do seu Pedido de Execução de Serviços de Limpeza\n' +
      '\n' + '* Subtotal Custo da Área: R$ {:.2f}\n'.format(custo_metragem) +
      '* Subtotal Custo do Tipo de Limpeza: R$ {:.2f}\n'.format(custo_limpeza) +
      '* Subtotal dos Serviços Adicionais: R$ {:.2f}\n'.format(contador_escolha) +
      '\n' +
      '* TOTAL DO PEDIDO R$ {:.2f}'.format(custo_metragem+custo_limpeza+contador_escolha))
"""
TESTES

    print(custo_metragem)
    print(custo_limpeza)
    print(contador_escolha)

"""
