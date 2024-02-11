# Escreva um programa que faça o computador perguntar 'Pensar'
# em um numero inteiro entre 0 e 5 e peça
# para o usuario tentar descobrir qual foi o
# numero escolhido pelo computador.
# O programa deve escrever na tela se o usuario acertou ou perdeu.

import random
sortRando = [0, 1, 2, 3, 4, 5]
numero = int(input('Informe um numero: '))
num = random.choice(sortRando)
print(num)
if num == numero:
    print('Voce acertou: {}'.format(num))
else:
    print('Voce Perdeu!: ')
