import random 

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

x = [a1, a2, a3, a4]
sorteio = random.choice(x)

print(f'{sorteio} irá apagar o quadro')