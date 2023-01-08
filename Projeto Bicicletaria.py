listaPeca = []
def cadastraPeca (codigo): #Função que cadastra as peças
    print('Código da peça 00{}'.format(codigo))
    ru4028367 = input('Por favor entre com o NOME da peça: ') #Variavel que define o nome da peça
    fabricante = input('Por favor entre com o FABRICANTE da peça: ') #Variavel que define o nome do fabricante
    valor = input('Por favor entre com o VALOR(R$) da peça: ') #Variavel que define o valor (R$)
    dicionarioPeca = {'peca'       :  ru4028367,    #Dicionario onde as peças irão ficar armazenadas
                      'fabricante' : fabricante,
                      'valor'      : valor,
                      'codigo'     : codigo }
    listaPeca.append(dicionarioPeca.copy())

def consultarPeca(): #Função de consultar peças
    while True:
        try:
            print('Você Selecionou a Opção de Consultar Peças')
            opConsultar = int(input('1 - Consultar Todas as Peças\n'
                                    '2 - Consulta Peças por Código\n'
                                    '3 - Consulta Peças por Fabricante\n'
                                    '4 - Retornar\n'
                                    '>>'))
            if opConsultar == 1: #Consultar todas as peças
                print('-' * 10)
                for nome in listaPeca:
                    for key, value in nome.items():
                        print('{} : {}'.format(key, value))
                print('-' * 10)
            elif opConsultar == 2: #Consultar peças por código
                print('-' * 10)
                entrada = int(input('Digite o código: '))
                for nome in listaPeca: #Função que faz a varredura para achar o código que o usuario quer consultar
                    if(nome['codigo'] == entrada):
                        for key, value in nome.items():
                           print('{} : {}'.format(key, value))
            elif opConsultar == 3: #Consultar peças por fabricante
                print('-' * 10)
                entrada = input('Digite o Fabricante: ')
                for nome in listaPeca: #Função que faz a varredura para achar o fabricante que o usuario quer consultar
                    if (nome['fabricante'] == entrada):
                        for key, value in nome.items(): #Função que faz a varredura para achar as peças que possuem o mesmo fabricante e poder printar na proxima linha
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4: #Sair da função de consultar peças
                break #Sai do laço caso uma das condições sejam satisfeitas...
            else: #Se não forem...
                print('Você digitou um valor fora das opções')
        except ValueError: #Se caso o usuario digitar uma opção com valor não numérico
            print('Valor incorreto')

def removerPeca(): #Função de remover as peças
    print('Você Selecionou a Opção de Remover Peça')
    entrada = int(input('Digite o codigo da peça a ser removida:'))
    for nome in listaPeca: #Função que faz a varredura para achar a peça que o usuario quer remover
        if (nome['codigo'] == entrada):
           listaPeca.remove(nome) #Função que remove o dicionario da peça de dentro da lista
codigo = 0 #Variavel que define os códigos das peças
print('Bem-vindo ao controle de estoque da bicicletaria do Filipe Vilela ')
while True: #Laço de repetição do Main do programa
    try:

        op = int(input('Escolha a opção desejada:\n'
                        '1 - Cadastrar peças\n'
                        '2 - Consultar peças \n'
                        '3 - Remover peças \n'
                        '4 - Sair\n'
                        '>>'))
        if op == 1: #Cadastro
         codigo = codigo + 1
         cadastraPeca(codigo)
        elif op == 2: #Consulta
            consultarPeca()
        elif op == 3: #Remover
            removerPeca()
        elif op == 4: #Encerrar programa
            print('Encerrando o programa ...')
            break #Sai do laço caso uma das condições sejam satisfeitas...
        else: #Se não forem...
          print('Opção invalida')
          continue #Retornar para o inicio do laço
    except ValueError: #Se caso o usuario digitar uma opção com valor não numérico
        print('Valor errado')
