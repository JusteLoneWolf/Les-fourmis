from Class.Player import Player # Appel de la class Player
from Class.Fourmis import Fourmi
from Class.Nouriture import Nouriture

class Game:
    def __init__(self):
        self.player = Player() # Initialise a la class player
        self.nouriture = Nouriture()
        self.press = {} # Les boutons

    def appear(self):
        Fourmi()