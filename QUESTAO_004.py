# Identificação: Programa Controle de Funcionários Alex de Andrade Nascimento
"""
Menu com Submenu
1.	Cadastrar Funcionário
2.	Consultar Funcionários(s)
    1)	Consultar Todas as Funcionários
    2)	Consultar Funcionário por Id
    3)	Consultar Funcionário(s) por Setor
    4)	Retornar
3.	Remover Funcionário
4.	Sair

"""
# criação da lista e variável global

lista_codigo_funcionario = list()
codigo_funcionario = 17


# criação da função borda
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




# função cadastrar_funcionario(id)

def funcao_cadastro_funcionario():
    print()
    dicionario_funcionario_funcao = {} # Dicionário que comporá a lista_codigo_funcionario
    dicionario_funcionario_funcao['codigo'] = codigo_funcionario
    dicionario_funcionario_funcao['nome'] = input('Nome do Funcionário: ').upper() #inserção do nome em maiúsculo
    dicionario_funcionario_funcao['setor'] = input('Setor do Funcionário: ').upper() #inserção do setor em maiúsculo
    dicionario_funcionario_funcao['salario'] = float(input('Salário do Funcionário: '))
    lista_codigo_funcionario.append(dicionario_funcionario_funcao)
    print('Cadastro do Funcionário {} do Setor {} realizado com sucesso! Código de registro: {}'.format(dicionario_funcionario_funcao['nome'], dicionario_funcionario_funcao['setor'], dicionario_funcionario_funcao['codigo']))

# Função de consulta

def funcao_consulta_funcionario():
    borda('Submenu Consultar')
    print()
    while True: # Laço para criação do Submenu
        print('1 - Consultar Todos os Funcionário\n' +
              '2 - Consultar Funcionário por Código\n' +
              '3 - Consultar Funcionário por Setor\n' +
              '4 - Retornar para o Menu Principal\n')
        escolha_submenu_consultar = input('Digite a opção desejada:\n' +
                                       '>> ')
        if escolha_submenu_consultar == '1':
            for funcionario in lista_codigo_funcionario: # varrer lista
                print('-'*40)
                for key, value in funcionario.items():
                    print('{}: {}'.format(key, value))
                print('-' * 40)
        elif escolha_submenu_consultar == '2':
            consultar_por_codigo = int(input('Digite o Código Único do Funcionário:\n'
                                             '>> '))
            for funcionario in lista_codigo_funcionario:
                if funcionario['codigo'] == consultar_por_codigo:
                    print('-' * 40)
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))
                    print('-' * 40)

        elif escolha_submenu_consultar == '3':
            consultar_por_setor = input('Digite o SETOR para consulta:\n'
                                             '>> ').upper()
            for funcionario in lista_codigo_funcionario:
                if funcionario['setor'] == consultar_por_setor:
                    print('-' * 40)
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))
                    print('-' * 40)

        elif escolha_submenu_consultar == '4':
            return
        else:
            print('Opção Inválida!\n')
            continue

# Função remover

def funcao_remover_funcionario():
    remover_funcionario = int(input('Digite o CÓDIGO Único do Funcionário:\n'
                                '>> '))
    for funcionario in lista_codigo_funcionario:
        if funcionario['codigo'] == remover_funcionario:
            lista_codigo_funcionario.remove(funcionario)
            print('O Funcionário {}  de CÓDIGO {} foi removido do Cadastro!'.format(funcionario['nome'], funcionario['codigo']))

borda('Bem-Vindo ao Controle de Funcionários Alex de Andrade Nascimento')

while True:
    print()
    print('1 - Cadastrar Funcionário\n' +
          '2 - Consultar Funcionário(s)\n' +
          '3 - Remover Funcionário\n' +
          '4 - Sair\n')
    escolha_menu_principal = input('Digite a opção desejada:\n' +
                               '>> ')
    if escolha_menu_principal == '4':
        borda('Obrigado! Programa Encerrado!')
        break # Encerra o laço
    elif escolha_menu_principal == '1':
        codigo_funcionario += codigo_funcionario + 13
        retorno_cadastro_funcionario = funcao_cadastro_funcionario()
    elif escolha_menu_principal == '2':
        consulta_funcionario = funcao_consulta_funcionario()
    elif escolha_menu_principal == '3':
        remover_funcionario = funcao_remover_funcionario()
    else:
        print('Opção Inválida!')
# Encerramento do Programa
