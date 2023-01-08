def dimensoesObjeto():
    global volume
    global valorVolume
    while True:
        try:
            comprimento = float(input('Digite o comprimento do objeto (em cm):'))
            largura = float(input('Digite a largura do objeto (em cm):'))
            altura = float(input('Digite a altura do objeto (em cm):'))
            volume = comprimento * largura * altura

            print('O volume do objeto é:{}'.format(volume))
            if volume < 1000:
                valorVolume = 10
            elif 1000 <= volume < 10000:
                valorVolume = 20
            elif 10000 <= volume < 30000:
                valorVolume = 30
            elif 30000 <= volume < 100000:
                valorVolume = 50
            else:
                print('Não aceitamos objetos tao grandes')
                continue
            break
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não númerico')
            print('Por favor entre com as dimensões desejadas novamente')
def pesoObjeto():
    global multiPeso
    while True:
        try:
            peso = float(input('Digite o peso do objeto (em kg): '))
            if peso <= 0.1:
               multiPeso = 1
            elif 0.1 < peso < 1:
                multiPeso = 1.5
            elif 1 < peso <= 10:
                multiPeso = 2
            elif 10 < peso < 30:
                multiPeso = 3
            else:
                print('Não aceitamos objetos tão pesados')
                continue
            break
        except ValueError:
            print('Você digitou um valor não numérico')

def rotaObjeto():
    global multiRota
    while True:
        try:
            print('Selecione a rota:')
            print(' BR - De Brasília para Rio de Janeiro')
            print(' BS - De Brasília para São Paulo')
            print(' RB - De Rio de Janeiro para Brasília')
            print(' RS - De Rio de Janeiro para São Paulo')
            print(' SR - De São Paulo para Rio de Janeiro')
            print(' SB - De São Paulo para Brasília')
            rota = input('>>')
            if rota == 'RS' or rota == 'SR':
                multiRota = 1
            elif rota == 'BS' or rota == 'SB':
                multiRota = 1.2
            elif rota == 'BR' or rota == 'RB':
                multiRota = 1.5
            elif rota != 'RS' or rota != 'BS' or rota != 'RB' or rota != 'RS' or rota != 'SR' or rota != 'SB':
                print('Você digitou uma rota que não existe')
                print('Por favor entre com a rota desejada novamente')
                continue

            break
        except:
            print('Você digitou uma rota que não existe')

valorVolume = 0
volume = 0
multiPeso = 0
multiRota = 0
print('Bem vindo a Companhia de Logística do Filipe Vilela')
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
valor = valorVolume * multiPeso * multiRota
print('Total a pagar (R$): {} (dimensões: {} * peso:{} * rota:{})'.format(valor, valorVolume, multiPeso, multiRota))