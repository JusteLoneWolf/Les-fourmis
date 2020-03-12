import pygame  # Installation "pip install pygame" avec la derniere version de python
from Class.Menu import MainMenu

import os


pygame.init()  # Initialisation

pygame.display.set_caption('Les fourmis','asset/fourmis/ant.png')  # Nomme le jeu
screen = pygame.display.set_mode((1280, 720))  # Forme la fenetre



# Bloucle infini
run = True  # Le jeu tourne ( ͡° ͜ʖ ͡°)

while run:  # "Moteur"
    MainMenu().build(screen)





    pygame.display.flip()

