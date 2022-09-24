''' Desenvolva uma lógica que leia os valores de A, B e C de uma equação do
segundo grau e mostre o valor de Delta. '''
print('calculadora de delta')
A = float(input("Insira o valor de A: "))
print('-----------------------------------')
B = float(input("Insira o valor de B: "))
print('-----------------------------------')
C = float(input("Insira o valor de C: "))
print('-----------------------------------')

D1 = B ** B
Delta = D1 - 4 * A * C
print(Delta)