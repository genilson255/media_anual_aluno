# Crie um programa que leia um numero inteiro e mostre na
# tela se é par ou impar

numero = int(input("Qual o numero?: "))
if numero % 2 == 0:
    print("O numero que voce escolheu é {} ele é Par".format(numero))
else:
    print("O numero que voce escolheu é {} ele é Ímpar".format(numero))
