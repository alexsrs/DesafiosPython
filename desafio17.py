import math
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catOposto, catAdjacente)
print('A hipotenusa {:.2f}'.format(hipotenusa))
