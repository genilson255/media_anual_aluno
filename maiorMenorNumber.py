# https://pt.stackoverflow.com/questions/199015/como-fazer-o-python-selecionar-o-maior-n%C3%BAmero-de-um-conjunto

lista = []
qtn = input('informe a qt de numeros: ')

for n in range(0, int(qtn)):
    lista.append(int(input('Digite o número: ')))
    print('Menor número da lista: ', min(lista))
    print('Maior número da lista: ', max(lista))
