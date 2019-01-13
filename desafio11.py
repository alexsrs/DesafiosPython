largura = float(input('Digite a largura da parede em metros: '))
altura =  float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A parede possui {:.2f}m² e você irá precisar de {:.1f} galões de tinta'.format(area,tinta))