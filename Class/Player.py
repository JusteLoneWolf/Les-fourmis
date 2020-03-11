import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.turn = 0
        self.maxTurn = 100
        self.holding = {'item': '', 'hold': False}
