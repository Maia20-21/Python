x = int(input('Escolha um número: '))
y = int(input('Escolha outro número: '))
s = x + y
print(f'A soma vale {s}')

n = float(input('Digite um valor: '))
print(n)

n2 = bool(input('Digite outro valor: '))
print(n2)

n3 = input('Digite algo: ') 
print('É numérico? ', n3.isnumeric())                                                            # é número?
 
n4 = input('Digite outra coisa: ')
print('É alfabético?', n4.isalpha())                                                             # é letra?

n5 = input('Digite algo de alguma coisa: ')
print('É composto por números ou letras? ', n5.isalnum())                                        # é letra ou número?

n6 = input('Digite uma palavra: ')
print('Esta tudo em letra maiúscula? ', n6.isupper())                                            # somente com letras maiúsculas?

n7 = input('Digite seu nome: ')
print('Está capitalizada? ', n7.istitle())                                                       

n8 = input('aperto o espaço e de "enter":')
print('Só tem espaços? ', n8.isspace())

