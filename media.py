b1 = float(input('Informe a media do primeiro bimestre: '))
b2 = float(input('Informe a media do segundo bimestre: '))
b3 = float(input('Informe a media do terceiro bimestre: '))
b4 = float(input('Informe a media do quarto bimestre: '))

nome = str(input("Nome do Aluno?:  "))

media = (b1 + b2 + b3 + b4) / 4

print('A soma das medias {}, {}, {}, {} É: Media: {}'
      .format(b1, b2, b3, b4, media))

if media >= 0 and media <= 5:
    print('{}, Voce esta reprovado com media {}'.format(nome, media))

elif media >= 6 or media <= 7:
    print('Sua media {} esta abaixo do esperado, {}'.format(media, nome))

elif media == 8 or media <= 9:
    print('Sua media foi {}. Parabéns, voce esta aprovado, {}'
          .format(media, nome))
elif media == 10:
    print("Parabens {} Voce obteve nota maxima".format(nome))
else:
    print('')
