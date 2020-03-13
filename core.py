import pygame  # Installation "pip install pygame" avec la derniere version de python
from Class.Menu import MainMenu
from render.game import Lunch
import sys


pygame.init()  # Initialisation

pygame.display.set_caption('Les fourmis','asset/fourmis/ant.png')  # Nomme le jeu
screen = pygame.display.set_mode((1280, 720))  # Forme la fenetre

print(pygame.font.get_fonts())

# Bloucle infini
run = True  # Le jeu tourne ( ͡° ͜ʖ ͡°)
menu = MainMenu()
isMenu = True
while run:  # "Moteur"
    if isMenu:
        menu.build(screen)
    elif isMenu is not True:
        menu.option(screen)

    for event in pygame.event.get():  # Get les event
        if event.type == pygame.QUIT:  # Si l'event quit est lance je ferme le jeu
            pygame.quit()  # Fermeture du jeux
            print('Fermeture... ')  # Envoi en console
            sys.exit(0)  # ferme le programme
        elif event.type == pygame.MOUSEBUTTONDOWN:  # quand je relache le bouton
            if event.button == 1:  # 1= clique gauche
                if menu.buttonStart.collidepoint(event.pos) and isMenu is not True :
                    print(1)
                    Lunch().lunch(screen)
                elif menu.buttonStart.collidepoint(event.pos):
                    isMenu = False
                    menu.option(screen)
                elif menu.buttonBack.collidepoint(event.pos):
                    print(2)
                    isMenu = True
                    menu.build(screen)
                elif menu.buttonQuit.collidepoint(event.pos):
                    pygame.quit()  # Fermeture du jeux
                    print('Fermeture... ')  # Envoi en console
                    sys.exit(0)  # ferme le programme



    pygame.display.flip()

