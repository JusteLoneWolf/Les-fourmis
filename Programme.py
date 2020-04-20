import Menu_Accueil

#On importe pygame et on l'initialise
import pygame
pygame.init()
couleur_blanc = (255,255,255)

#On définit l'écran
screen = pygame.display.set_mode((1200, 950))
screen.fill(couleur_blanc)

#L'application se lance
Menu_Accueil.menu()     #On ouvre le menu

print("Programme terminé")



