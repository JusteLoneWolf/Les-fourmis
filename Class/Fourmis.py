import pygame
from pygame import *
from random import randint
class Fourmi(pygame.sprite.Sprite): # appel de la super class Sprite

    def __init__(self):
        super().__init__()
        self.turn = 0 # Nombre de tours de la fourmie
        self.maxTurn = 100 # Nombre max de tour
        self.holding = {'item': '', 'hold': False} # Si elle rien un objet
        self.speed = 10 # Sa vitesse
        self.playerImage = pygame.image.load('./asset/fourmis/ant_player.png').convert() # La fourmie
        self.playerImage = pygame.transform.scale(self.playerImage, (50, 50)) # resize de la fourmie
        self.rect = self.playerImage.get_rect(center = (150, 150)) # Capture des coordoné de la fourmie
        self.rect.x = 400 # Cadrage de la fourmie
        self.rect.y = 400# Cadrage de la fourmie
        # self.originimg = self.playerImage
        self.test = False

        self.horloge = pygame.time.Clock()

        def mouv_alea():
            num = randint(1,4)
            if num == 1:
                move_r()
            elif num == 2:
                move_d()
            elif num == 3:
                move_u()
            elif num == 4:
                move_l()
            self.horloge.tick(90)

        def move_r():  # Bouge a droite
            # self.playerImage = pygame.transform.rotate(self.playerImage, 90)
            self.rect.x += self.speed

        def move_l():  # bouge da gauche
            # self.playerImage = pygame.transform.rotate(self.playerImage,270)
            self.rect.x -= self.speed

        def move_d():  # bouge a bas
            # self.playerImage = pygame.transform.rotate(self.playerImage, 180)
            self.rect.y += self.speed

        def move_u():  # boiuge a haut
            # self.playerImage = pygame.transform.rotate(self.playerImage, 0)
            self.rect.y -= self.speed
