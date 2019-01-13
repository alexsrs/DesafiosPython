dias = int(input('Informe o número de dias da locação: '))
km = float(input('Qual a kilometrage percorrida ? '))
valor = (dias * 60) + (km * 0.15)
print('O valor a pagar é R$ {:.2f}'.format(valor))
