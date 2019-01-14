from random import choice
n1 = str(input('Digite o nome do 1° Aluno: '))
n2 = str(input('Digite o nome do 2° Aluno: '))
n3 = str(input('Digite o nome do 3° Aluno: '))
n4 = str(input('Digite o nome do 4° Aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

