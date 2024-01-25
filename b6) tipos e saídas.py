x = int(input('Escolha um número: '))
y = int(input('Escolha outro número: '))
s = x + y
print(f'A soma vale {s}')

n = float(input('Digite um valor: '))
print(n)

n2 = bool(input('Digite outro valor: '))
print(n2)

n3 = input('Digite algo: ') 
print(n3.isnumeric())                                          # é número?
 
n4 = input('Digite outra coisa: ')
print(n4.isalpha())                                            # é letra?

n5 = input('Digite algo de alguma coisa: ')
print(n5.isalnum())                                            # é letra ou número?

n6 = input('Digite uma palavra: ')
print(n6.isupper())                                            # somente com letras maiúsculas?
