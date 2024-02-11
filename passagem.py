# Desenvolva um programa que pergunte a distancia de uma viagem em KM.
# Calcule o preço da pasagem, cobrando R$:0,50 por km para viagem de ate 200km
# e R$:0.45 para viagens mais longas

distancia = float(input('Qual a distancia em km/h?: '))

viagem = 0
if distancia <= 200:
    viagem = distancia * 0.50
    print('{}KM total a ser pago em real é de: R$:{} reais'.format(distancia, viagem))
elif distancia > 200:
    viagem = (distancia * 0.45)
    print('{}KM rodado, Valor a ser pago em real é de: R$:{} reais'.format(distancia, viagem))
else:
    print("...")
