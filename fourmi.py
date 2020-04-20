import pygame

class Fourmi(pygame.sprite.Sprite): #Cette classe permet de créer et gérer une fourmi

    def __init__(self, taille, Pas, NBTourSansManger, nom):     #On l'initialise ici
        super().__init__()  #On commence par initialiser la classe Sprite, qui signifie que notre objet en est lui-même un
        self.image = pygame.transform.scale(pygame.image.load("fourmi.png"), (int(Pas), int(Pas)))      #On lui attribue une image, que l'on redimensionne
        self.rect = self.image.get_rect()       #On associe à notre objet un rect
        if(taille%2==0):        #Qui sera placé au milieu de la grille
            self.rect.x = float(taille/2 * Pas)     
            self.rect.y = float(120+ taille/2 * Pas)        
        else:
            self.rect.x = float((taille+1)/2 * Pas)
            self.rect.y = float(120+ ((taille+1)/2 * Pas))
        self.Faim = NBTourSansManger       #Son nombre de tour sans manger dépend des paramètres
        self.TourMaxRestant = 100       #Son nombre de tour maximum est 100
        self.vie = True         #A sa création, la fourmi est en vie
        self.Nom = nom      #Et elle possède un nom qui dépend des paramètres
        
        
    #Les fonction suivantes gèrent le déplacement de la fourmi
    def MoveRight(self,Pas):            
        self.rect.x += float(Pas)       #Déplcament à droite
        
    def MoveLeft(self,Pas):
        self.rect.x -= Pas          #Déplacement à gauche

    def MoveTop(self,Pas):
        self.rect.y -= Pas          #Déplacement en haut

    def MoveDown(self,Pas):
        self.rect.y += Pas          #Déplacement en bas
