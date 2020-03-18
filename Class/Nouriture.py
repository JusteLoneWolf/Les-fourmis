import pygame

class Nouriture:
    def __init__(self):
        self.image= pygame.image.load('./asset/nourriture/fruit.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # resize de la fourmie
        self.Imagerect = self.image.get_rect(center=(150, 150))
        self.Imagerect.x = 350  # Cadrage de la fourmie
        self.Imagerect.y = 400  # Cadrage de la fourmie