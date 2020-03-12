from Class.Player import Player # Appel de la class Player

import pygame

class Game:
    def __init__(self):
        self.player = Player() # Initialise a la class player
        self.press = {} # Les boutons
