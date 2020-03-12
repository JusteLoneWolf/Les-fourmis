import pygame
from render.game import Lunch
import sys
class MainMenu:
    def __init__(self):
        self.color ={"red":(156, 0, 0),"green":(0, 493, 0),"blue":(0, 0, 209)}
        self.mixColor = (self.color['red'],self.color['green'],self.color['blue'])
        self.ChoosColor = 0

        self.start_game =  [(50,650), (200, 50)]
        self.quit = [(1050,650), (110, 50)]

        self.text_property = {"color":(56,63,66),"pos":(80, 655)}
        self.Font = {"Main":pygame.font.Font('asset/font/punch.ttf',30),"Title":pygame.font.Font('asset/font/punch.ttf',120)}
        self.title=self.Font["Title"].render("Les Fourmis",True,self.text_property["color"])

        self.Starttext = self.Font["Main"].render('Start game',True,self.text_property["color"])
        self.Quittext = self.Font["Main"].render('Quit', True, self.text_property["color"])

        self.rect = {"text" :self.Starttext.get_rect(),"title":self.title.get_rect(),"quit":self.Quittext.get_rect()}
        self.rect["text"].center=(self.text_property["pos"])
        self.rect["quit"].center = (1075,660)
        self.rect["title"].center = (400,20)

        self.centerText = self.rect["text"].center
        self.centerTitle = self.rect["title"].center
        self.centerQuit = self.rect["quit"].center

        self.back = pygame.image.load('asset/back/fourmis.jpg')

        self.buttonStart = pygame.Rect(self.start_game)
        self.buttonQuit = pygame.Rect(self.quit)

        self.QuitrectSurf = pygame.Surface(self.buttonQuit.size)
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

        for event in pygame.event.get():  # Get les event
            if event.type == pygame.QUIT:  # Si l'event quit est lance je ferme le jeu
                pygame.quit()  # Fermeture du jeux
                print('Fermeture... ')  # Envoi en console
                sys.exit(0)  # ferme le programme
            elif event.type == pygame.MOUSEBUTTONUP:  # quand je relache le bouton
                if event.button == 1:  # 1= clique gauche
                    if self.buttonStart.collidepoint(event.pos):
                        Lunch().lunch(screen)
                    elif self.buttonQuit.collidepoint(event.pos):
                        pygame.quit()  # Fermeture du jeux
                        print('Fermeture... ')  # Envoi en console
                        sys.exit(0)  # ferme le programme

