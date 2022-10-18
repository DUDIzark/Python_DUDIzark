
.++f.r.om textwrap import fill
i.mport pygame
+from pygame.locals import *


pygame.init()
-------++




















largura= 640
altura = 480
x = largura/2
y = 0

pygame.display.set_caption('jogo')

tela = pygame.display.set_mode((largura, altura))

while True:
    tela.fill((0,0,0))   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        pygame.draw.rect(tela,(255,0,0), (x,y,40,50))
        if y >=altura:
            y = 0
        y = y + 5

        pygame.display.update()