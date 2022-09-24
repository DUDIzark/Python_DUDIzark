#desenvolva um programa que leia uma distancia e mostre os valores relativos em outra medidas
''' Desenvolva um programa que leia uma distância em metros e mostre os
valores relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72 A
distância de 85.7m corresponde a:
0.18572Km      1857.2dm
1.8572Hm       18572.0cm
18.572Dam      185720.0mm  '''
print('----------------------------------------')
m = float(input("Insira uma distancia em metros: "))
print('----------------------------------------')
km = m / 1000
hm = m / 100
dam = m / 10
print('----------------------------------------')
dm = m * 10
cm = m * 100
mm = m * 1000

print("A distancia {}, convertida o valor vai ficar: ".format(m))
print('----------------------------------------')
print("KM: \033[0;32m{}km\033[0;0m".format(km))
print('----------------------------------------')
print("HM: \033[0;32m{}hm\033[0;0m".format(hm))
print('----------------------------------------')
print("DAM: \033[0;32m{}dam\033[0;0m".format(dam))
print('----------------------------------------')
print("---------------")
print("DM: \033[0;32m{}dm\033[0;0m".format(dm))
print('----------------------------------------')
print("Cm: \033[0;32m{}cm\033[0;0m".format(cm))
print('----------------------------------------')
print("MM: \033[0;32m{}mm\033[0;0m".format(mm))
print('----------------------------------------')