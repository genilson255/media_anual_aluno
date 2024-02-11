# Escreva um programa que pergunte o salario de um funcionario e calcule o
# valor do aumento
# Para salarios superior a R$: 1.250,00 calcule um aumento de 10%
# Para salarios inferior ou igual, o auento é de 15%

print('======INICIO=======')
salario = float(input('Qual o salario do funcionario?: R$:'))
if salario < 0 or salario is None:
    print('Informe um valor valido! ')
elif salario > 1250:
    total = (salario * 0.10) + salario
    aumento = total - salario
    print('Aumento', aumento)
    print('O salario informado foi R$:{:.2f}, com o aumento passou a ser: R$:{:.2f}'.format(salario, total))
elif salario <= 1250:
    total = (salario * 0.15) + salario
    aumento = total - salario
    print('Aumento', aumento)
    print('O salario informado foi R$:{:.2f}, com o aumento passou a ser: R$:{:.2f}'.format(salario, total))
else:
    print()
print("======FIM=======")
