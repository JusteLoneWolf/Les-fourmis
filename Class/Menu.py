import pygame
from render.game import Lunch
import sys
import time

class MainMenu:
    def __init__(self):
        self.color ={"red":(0, 0, 0),"green":(0, 0, 0),"blue":(0, 0, 0)}
        self.mixColor = (self.color['red'],self.color['green'],self.color['blue'])
        self.ChoosColor = 0

        self.start_game =  [(50,650), (200, 50)]
        self.quit = [(1050,650), (110, 50)]

        self.text_property = {"color":(255,255,255),"pos":(70, 645)}
        self.Font = {"Main":pygame.font.SysFont('mvboli',30),"Title":pygame.font.SysFont('mvboli',120)}
        self.title=self.Font["Title"].render("Les Fourmis",True,self.text_property["color"])

        self.Starttext = self.Font["Main"].render('Start game',True,self.text_property["color"])
        self.Quittext = self.Font["Main"].render('Quit', True, self.text_property["color"])
        self.Backtext = self.Font["Main"].render('Back', True, self.text_property["color"])

        self.rect = {"text" :self.Starttext.get_rect(),"title":self.title.get_rect(),"quit":self.Quittext.get_rect(),'back':self.Quittext.get_rect()}
        self.rect["text"].center=(self.text_property["pos"])
        self.rect["quit"].center = (1075,650)
        self.rect["back"].center = (1075, 650)
        self.rect["title"].center = (350,20)

        self.centerText = self.rect["text"].center
        self.centerTitle = self.rect["title"].center
        self.centerQuit = self.rect["quit"].center
        self.centerBack = self.rect["back"].center

        self.back = pygame.image.load('asset/back/fourmis.jpg')

        self.buttonStart = pygame.Rect(self.start_game)
        self.buttonQuit = pygame.Rect(self.quit)
        self.buttonBack = pygame.Rect(self.quit)

        self.QuitrectSurf = pygame.Surface(self.buttonQuit.size)
        self.BackrectSurf = pygame.Surface(self.buttonQuit.size)
        self.StartrectSurf = pygame.Surface(self.buttonStart.size)

    def build(self,screen):
        screen.fill(0)
        self.StartrectSurf.fill(self.mixColor[self.ChoosColor])
        self.QuitrectSurf.fill(self.mixColor[self.ChoosColor])

        screen.blit(self.back, (0, 0))
        screen.blit(self.StartrectSurf, self.buttonStart)
        screen.blit(self.QuitrectSurf, self.buttonQuit)

        screen.blit(self.Starttext, self.centerText)
        screen.blit(self.title, self.centerTitle)
        screen.blit(self.Quittext, self.centerQuit)

    def option(self,screen):
        screen.fill(0)
        self.StartrectSurf.fill(self.mixColor[self.ChoosColor])
        self.BackrectSurf.fill(self.mixColor[self.ChoosColor])

        screen.blit(self.back, (0, 0))
        screen.blit(self.StartrectSurf, self.buttonStart)
        screen.blit(self.BackrectSurf, self.buttonBack)

        screen.blit(self.Starttext, self.centerText)
        screen.blit(self.Backtext, self.centerBack)

