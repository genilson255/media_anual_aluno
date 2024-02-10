b1 = int(input('Informe a media do primeiro bimestre: '))
b2 = int(input('Informe a media do segundo bimestre: '))
b3 = int(input('Informe a media do terceiro bimestre: '))
b4 = int(input('Informe a media do quarto bimestre: '))

media = (b1 + b2 + b3 + b4) / 4
print('A soma das medias {}, {}, {}, {} É: Media: {}'
      .format(b1, b2, b3, b4, media))
