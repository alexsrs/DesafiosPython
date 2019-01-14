import math
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O SENO de {}° é {:.2f}'.format(angulo, seno))
print('o seu COSSENO é {:.2f} e sua TANGENTE {:.2f}'.format(cosseno, tangente))