##Faça um algoritmo que leia a largura e altura de uma parede, calcule e
##sabendo que cada litro de tinta pinta uma área de 2metros quadrados. '

print('aplicativo que mede quantos metros vc precisa para pintar')
Largura = float(input("Insira a Largura da Parede: "))
print('--------------------------------------------------')
Altura = float(input("Insira a Altura da Parede: "))
print('--------------------------------------------------')
Area = Largura * Altura
Tinta = Area / 2

print("Para uma Area de {} metros, sera nescessario {} Litros de tinta.".format(Area, Tinta))