#15)	Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.  
from time import sleep


print('-------------------------sala do patrao------------------------------')
dias3=int(input('escreva a quantidades de dias que o funcionario trabalhou:'))
print('-------------------------------------------------------------------')

print('carregando uma nova pasta..📂📂')
salario = (dias3 * 25) * 8

print('-------------------------------------------------------------------')
print(' o salario da pessoa ficou: ', salario ,' sem taxas e nem multas ')