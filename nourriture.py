import pygame
from random import *

class Nourriture(pygame.sprite.Sprite):     #Cette classe permet de créer une nourriture

    def __init__(self, X, Y, Pas, PosNourriture, nom):      #On l'initialise ici
        super().__init__()     #On commence par initialiser la classe Sprite, qui signifie que notre objet en est lui-même un
        self.image = pygame.transform.scale(pygame.image.load("Nourriture.jpg"), (int(Pas), int(Pas)))      #On lui attribue une image, que l'on redimensionne
        self.rect = self.image.get_rect()       #On associe à notre objet un rect
        self.rect.x = X     #Dont la position dépend des paramètres donnés 
        self.rect.y = Y
        self.mange=False     #A sa création, la nourriture n'est pas encore mangée
        self.Nom = nom      #Et elle possède un nom, qui dépend des paramètres donnés
        
        
    