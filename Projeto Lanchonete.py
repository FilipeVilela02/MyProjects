cq = 9.00 #Variavel que define o valor (R$) do Cachorro Quente
cqd = 11.00 #Variavel que define o valor (R$) do Cachorro Quente Duplo
xe = 12.00 #Variavel que define o valor (R$) do X-Egg
xs = 12.00 #Variavel que define o valor (R$) do X-Salada
xb = 14.00 #Variavel que define o valor (R$) do X-Bacon
xt = 17.00 #Variavel que define o valor (R$) do X-Tudo
rl = 5.00 #Variavel que define o valor (R$) do Refrigerante Lata
cg = 4.00 #Variavel que define o valor (R$) do Chá Gelado
ru4028367 = '1' #Variavel que define resposta
valor = 0.0 #Variavel que define o valor

print('Bem vindo a Lanchonete do Filipe Vilela')
print('*' * 15 + ' Cardapio ' + '*' * 15)
print('| Código |       Descrição       | Valor |\n'
      '|  100   |   Cachorro Quente     |  9,00 |\n'
      '|  101   | Cachorro Quente Duplo | 11,00 |\n'
      '|  102   |        X-Egg          | 12,00 |\n'
      '|  103   |        X-Salada       | 12,00 |\n'
      '|  104   |        X-Bacon        | 14,00 |\n'
      '|  105   |        X-Tudo         | 17,00 |\n'
      '|  200   |   Refrigerante Lata   |  5,00 |\n'
      '|  201   |       Chá Gelado      |  4,00 |\n')

while ru4028367 == '1': #Estrutura de repetição
    cod = input('Entre com o codigo desejado: ')
    if cod == '100':
        print('Você pediu um Cachorro Quente no valor de: R$ {:.2f} '.format(cq))
        valor += cq
    elif cod == '101':
        print('Você pediu um Cachorro Quente Duplo duplo no valor de: R$ {:.2f}'.format(cqd))
        valor += cqd
    elif cod == '102':
        print('Você pediu um X-Egg no valor de: R$ {:.2f}'.format(xe))
        valor += xe
    elif cod == '103':
        print('Você pediu um X-Salada no valor de: R$ {:.2f}'.format(xs))
        valor += xs
    elif cod == '104':
        print('Você pediu um X-Bacon no valor de: R$ {:.2f}'.format(xb))
        valor += xb
    elif cod == '105':
        print('Você pediu um X-Tudo no valor de: R$ {:.2f}'.format(xt))
        valor += xt
    elif cod == '200':
        print('Você pediu um Refrigerante Lata no valor de: R$ {:.2f}'.format(rl))
        valor += rl
    elif cod == '201':
        print('Você pediu um Chá Gelado no valor de R$ {:.2f}'.format(cg))
        valor += cg
    else:
        print('Código invalido!')

    ru4028367 = input('Deseja pedir algo mais\n' #Variavel que recebe a resposta do usuario
                 '1 - Sim\n'
                 '0 - Não\n'
                 '>>')

    while ru4028367 != '0' and ru4028367 != '1':

        ru4028367 = input('Código invalido\n'
                     'Deseja pedir algo mais?\n'
                     '1 - Sim\n'
                     '0 - Não\n'
                     '>>')
        if ru4028367 == '0':
            break #break para se caso as condiçoes do laço forem satisfeitas...
        else: #E se não forem...
            continue #Reiniciar o laço.


print('O valor total a ser pago é: R$ {:.2f}'.format(valor))

