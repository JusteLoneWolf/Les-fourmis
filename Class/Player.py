import pygame


class Player(pygame.sprite.Sprite): # appel de la super class Sprite

    def __init__(self):
        super().__init__()
        self.turn = 0 # Nombre de tours de la fourmie
        self.maxTurn = 100 # Nombre max de tour
        self.holding = {'item': '', 'hold': False} # Si elle rien un objet
        self.speed = 20 # Sa vitesse
        self.playerImage = pygame.image.load('./asset/fourmis/ant_player.png') # La fourmie
        self.playerImage = pygame.transform.scale(self.playerImage, (50, 50)) # resize de la fourmie
        self.rect = self.playerImage.get_rect() # Capture des coordoné de la fourmie
        self.rect.x = 400 # Cadrage de la fourmie
        self.rect.y = 400# Cadrage de la fourmie
        # self.originimg = self.playerImage

    def move_r(self): # Bouge a droite
       # self.playerImage = pygame.transform.rotate(self.playerImage, 90)
        self.rect.x += self.speed

    def move_l(self): #bouge da gauche
        # self.playerImage = pygame.transform.rotate(self.playerImage,270)
        self.rect.x -= self.speed

    def move_d(self): # bouge a bas
        # self.playerImage = pygame.transform.rotate(self.playerImage, 180)
        self.rect.y += self.speed

    def move_u(self): #boiuge a haut
        # self.playerImage = pygame.transform.rotate(self.playerImage, 0)
        self.rect.y -= self.speed

# Le reste commente sont encore en test (c'est pour faire tourné la foumis dans le sens ou elle marche sauf que ca marche pas tellement encore