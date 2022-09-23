##16)	[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.    

print('prazer eu sou o medico paulo tejando, vou te entregar um questionario para voce responder')
print('-----------------------------------------------------------------------------------------')
anos=int(input('quantos anos o senhor fuma?:'))
dia=int(input('fuma quantos cigarros por dia?:'))
cigarros = dia * 365 
cigarrostudo = cigarros * anos 
perdeu = 10 * cigarrostudo
cigarrosdias = perdeu / 1440
print('-----------------------------------------------------------------------------------------')

print('voce perdeu  {:.0f} dias da sua vida, procure um medico imediatamente'.format(cigarrosdias))

