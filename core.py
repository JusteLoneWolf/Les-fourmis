import pygame # Installation "pip install pygame" avec la derniere version de python
from Class import Player
pygame.init()

pygame.display.set_caption('Les fourmis')
fenetre = pygame.display.set_mode((640, 480))

run = True
while run:
    print(Player.Player().holding)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print('Fermeture... ')
