print('desconto dos 5%')
print('---------------------------------------------------')
preco = float(input("Insira o preco do produto: "))
desconto = preco - (preco * 5 / 100)

print("O preco final do produto com 5% de desconto sera: \033[0;32m{}\033[0;0m".format(desconto))