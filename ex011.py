largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
tinta = area / 2
print('Para pintar uma parede com {:.2f} m², será necessário {:.2f} litros de tinta'.format(area, tinta))

