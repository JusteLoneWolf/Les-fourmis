import pygame
from random import *

class Obstacle(pygame.sprite.Sprite):     #Cette classe permet de créer un obstacle

    def __init__(self, X, Y, Pas, Nom):      #On l'initialise ici
        super().__init__()     #On commence par initialiser la classe Sprite, qui signifie que notre objet en est lui-même un
        self.image = pygame.transform.scale(pygame.image.load("asset/obstacle.jpg"), (int(Pas), int(Pas)))      #On lui attribue une image, que l'on redimensionne
        self.rect = self.image.get_rect()       #On associe à notre objet un rect
        self.rect.x = X     #Dont la position dépend des paramètres donnés 
        self.rect.y = Y
        self_nom = Nom
  
        
        
    