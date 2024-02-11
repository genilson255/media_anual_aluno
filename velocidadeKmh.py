# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma msg dizendo que ele foi multado.
# A Multa vai custar R$:7.00 por cada km acima da velocidade

speed = float(input("Qual a velocidade atual?: "))
print('A velocidade é: {}km/h'.format(speed))
taxa = 7.00
multa = 0
excesso = speed - 80
if speed > 80:
    multa = (speed - 80) * taxa
    print("Limite de velocidade permitido ultrapassado {}KM/h".format(excesso))
    print('Voce multado em R$:{:.2f}'.format(multa))
