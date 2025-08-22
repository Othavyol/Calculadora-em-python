numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
subtração = numero1 - numero2
multiplicação = numero1 * numero2
divisão = numero1 / numero2

print('\nESCOLHA UMA DAS ALTERNATIVAS ABAIXO PARA EXIBIR O RESULTADO:\n\n')

print(' 1 - SOMA\n 2 - SUBTRAÇÃO\n 3 - MULTIPLICAÇÃO\n 4 - DIVISÃO\n')

escolha = input('selecione um numero para fazer a conta: ')

if escolha == '1':
    print(f'o resumtado da sua soma foi de {soma}')

elif escolha == '2':
    print(f'o resumtado da sua subtração foi de {subtração}')

elif escolha == '3':
    print(f'o resumtado da sua multiplicação foi de {multiplicação}')

elif escolha == '4':
    print(f'o resumtado da sua divisão foi de {divisão}')

else:
    print('Esse valor esta errado, tente novamente!')
