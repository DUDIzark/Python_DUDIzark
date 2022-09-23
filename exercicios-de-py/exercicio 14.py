##14)	A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado. 
print('-----------------------$-$-locadora de carros semi novos-$-$------------------------------')
quantidade2 =int(input('qual a quantidade de KM foi percorrido nesse carro:'))
dias2 =float(input('quantos dias esse carro ficou alugado:'))

quantidade = dias2 * 90
dias = quantidade2 * 0.20
valor = quantidade + dias

print('-----------------$$$$--------sala de pagamento------------$$$$----------------------------')
print('o resultado deu' , quantidade , 'reais!! ', dias2 , 'com mais essas taxas ficou:' , valor ,)