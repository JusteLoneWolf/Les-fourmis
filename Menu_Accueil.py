import pygame
import Simulation


pygame.init()
#On définit quelques couleurs
couleur_bleu = (89, 152, 255)
couleur_noir = (0,0,0)
couleur_blanc = (255,255,255)

#On définit notre surface (la fenêtre), en lui attribuant une taille et un fond blanc
screen = pygame.display.set_mode((1200, 950))


#On définit des polices de texte, en indiquant laquelle on utilise ainsi que la taille de police
police_arial = pygame.font.SysFont("arial", 50)
police_arial2 = pygame.font.SysFont("arial", 25)

#On créé du texte, en indiquant la police que l'on souhaite utiliser, le texte, et sa couleur. Le "True" indique qu'on lisse les contours
nom_jeu = police_arial.render("Projet fourmi", True, couleur_noir)
param_taille = police_arial2.render("Taille de la grille :", True, couleur_noir)
param_nbObstacle = police_arial2.render("Nombre d'obstacles :", True, couleur_noir)
param_nbMaxFourmis = police_arial2.render("Nombre maximum de fourmis :", True, couleur_noir)
param_nbTourMaxMortSansManger = police_arial2.render("Nombre de tour avant de mourir de faim :", True, couleur_noir)
param_posNourriture = police_arial2.render("Nourriture positionnée...", True, couleur_noir)
param_posNourriture1 = police_arial2.render("par défaut", True, couleur_noir)
param_posNourriture2 = police_arial2.render("aléatoirement", True, couleur_noir)
erreur = police_arial2.render("Vous devez saisir un nombre", True, couleur_noir)
text_Start = police_arial.render("Start", True, couleur_noir)
erreur_Start = police_arial2.render("Vous devez remplir tous les champs", True, couleur_noir)
Fois = police_arial2.render("x", True, couleur_noir)

#On créé des rectangles avec leur position et leur taille
rectangle_Taille= (250, 385, 100, 50)
rectangle_nbObstacle= (300, 485, 100, 50)
rectangle_nbMaxFourmis= (400, 585, 100, 50)
rectangle_tourSansManger= (525, 685, 100, 50)
rectangle_Defaut= (390, 785, 140, 50)
rectangle_Aleatoire= (575, 785, 200, 50)
rectangle_NotError= (550, 350, 400, 100)
rectangle_Start= (1000, 800, 200, 200)



#On définit une image, puis on la convertit pour la rendre plus facilement traitable par Pygame
image_fond = pygame.image.load("fond_menu.jpg")
image_fond.convert()

#On définit des positions, qui serviront à placer le texte
x1=255
y1=400

x2 = 305 
y2 = 500

x3 = 405 
y3 = 600

x4 = 530 
y4 = 700

#On créé des variables, qui permettront de stocker le choix de l'utilisateur
taille = ""
nbObstacle = ""
nbMaxFourmis = ""
nbTourMaxMortSansManger = ""
posNourriture = ""

#Pour l'instant, l'utilisateur ne peut pas écrire

ecriture = False
Menu = True
def menu():
    #Puis on les dessine sur la surface définit plus haut, en leur attribuant une couleur et une épaisseur de contours
    pygame.draw.rect(screen, couleur_noir, rectangle_Taille, 2)
    pygame.draw.rect(screen, couleur_noir, rectangle_nbObstacle, 2) 
    pygame.draw.rect(screen, couleur_noir, rectangle_nbMaxFourmis, 2) 
    pygame.draw.rect(screen, couleur_noir, rectangle_tourSansManger, 2)
    pygame.draw.rect(screen, couleur_noir, rectangle_Start, 5)
    
    pygame.draw.rect(screen, (191, 191, 191), rectangle_Defaut)
    pygame.draw.rect(screen, (191, 191, 191), rectangle_Aleatoire)
    
    #On définit comme globales les variables initialisées hors de la fonction, pour pouvoir les utiliser
    global Menu, ecriture, taille,nbObstacle, nbMaxFourmis, nbTourMaxMortSansManger, nbTourMaxMortSansManger, posNourriture, x1, y1, x2, y2, x3, y3, x4, y4, NumeroRect
    while Menu == True:
        for event in pygame.event.get(): #Pour chacun des évènement que pygame.get() récupère
                    if event.type == pygame.QUIT:      #Si quitte la fenêtre ouverte par pygame
                        Menu = False     #Alors le menu se ferme
                    elif event.type == pygame.MOUSEBUTTONDOWN:      #Si on fait un clic de souris                      
                        if pygame.Rect(rectangle_Taille).collidepoint(event.pos):    #Et que le clic s'est fait dans le carré qui correspond à la taille de la grille
                            ecriture = True     #Alors l'utilisateur peut écrire
                            NumeroRect = 1      #Et on enregistre qu'il se trouve dans le rectange correspondant à la taille de la grille
                        elif pygame.Rect(rectangle_nbObstacle).collidepoint(event.pos): #Ainsi de suite pour ce rectangle
                            ecriture = True
                            NumeroRect = 2
                        elif pygame.Rect(rectangle_nbMaxFourmis).collidepoint(event.pos): #Celui la
                            ecriture = True
                            NumeroRect = 3
                        elif pygame.Rect(rectangle_tourSansManger).collidepoint(event.pos): #Et lui
                            ecriture = True
                            NumeroRect = 4
                        elif pygame.Rect(rectangle_Defaut).collidepoint(event.pos): #Ici, on indique que si on clique sur le rectangle correspondant à "par défaut"
                            pygame.draw.rect(screen, couleur_noir, rectangle_Defaut, 2) #Alors on entoure le texte "par défaut" d'un rectangle noir
                            pygame.draw.rect(screen, couleur_blanc, rectangle_Aleatoire, 2) #Et "aléatoire" avec un rectangle blanc
                            posNourriture = "Defaut"    #On enregistre dans une variable le choix de l'utilisateur
                            ecriture = False       #On désactive l'éctiture, car ce paramètre ne necessite aucune saisie 
                        elif pygame.Rect(rectangle_Aleatoire).collidepoint(event.pos): #Même principe avec "aléatoire"
                            pygame.draw.rect(screen, couleur_blanc, rectangle_Defaut, 2) 
                            pygame.draw.rect(screen, couleur_noir, rectangle_Aleatoire, 2)
                            posNourriture = "Aleatoire"
                            ecriture = False
                        elif pygame.Rect(rectangle_Start).collidepoint(event.pos):  #Si on clique sur le rectangle correspondant au "Start"
                            List_Test = [taille, nbObstacle, nbMaxFourmis, nbTourMaxMortSansManger, posNourriture] #On créé une liste composée des variables paramétrables 
                            champs_rempli = 0  #On initialise le nombre de champs remplis à 0
                            for element in List_Test:  #On créé une boucle qui parcoure tous les éléments de la liste précédemment créée
                                if element != "":  #Si l'élement n'est pas vide (donc si on l'a paramétré)
                                    champs_rempli += 1   #Alors le nombre de champs remplis augmente de 1
                            if champs_rempli==5:        #Si le nombre de champs rempli est égal à 5, c'est à dire si tout les éléments on été paramétrés
                                Menu = False
                                print("On passe à la simulation")   #Alors on quitte le menu, et on passe à la simulation
                                print("Voici les choix de l'utilisateur")
                                print("Taille :",taille, "x", taille)
                                print("Nombre d'obstacles :", nbObstacle)
                                print("Nombre maximum de fourmis :", nbMaxFourmis)
                                print("Nombre de tour maximum sans manger :", nbTourMaxMortSansManger)
                                print("Positionnement de la nourriture :", posNourriture)
                                Simulation.Sim_Fourmiliere(taille, nbObstacle, nbMaxFourmis, nbTourMaxMortSansManger, posNourriture)
                                
                                
                            else:   #Sinon
                                screen.blit(erreur_Start, [600,475])        #On affiche un message d'erreur
                                ecriture = False        #On désactive l'écriture, elle pourra être activée en cliquant sur un champs paramétable
                        else:  #Si on ne clique sur aucun des éléments ci-dessus
                            ecriture = False #Alors on ne peut pas écrire
                            
                    elif event.type == pygame.KEYDOWN and ecriture == True:  #Si on appuie sur une touche, et que l'écriture est activée
                        try:
                            Chiffre = int(event.unicode)   #On vérifie que la saisie est bien un chiffre
                            pygame.draw.rect(screen, couleur_blanc, rectangle_NotError)    #On recouvre les potentiels anciens messages d'erreur avec un rectangle blanc (méthode infaillible)
                            saisi = police_arial2.render(event.unicode, True, couleur_noir)     #On créé du texte, qui correspond au chiffre saisi
                            if(NumeroRect == 1):    #Si on se situe dans le rectangle de la taille
                                screen.blit(saisi, [x1,y1])     #On affiche la saisi dans ce dernier
                                screen.blit(saisi, [x1+150,y1]) 
                                taille += str(event.unicode)    #Et on enregistre ce choix dans la variable taille
                                x1+=20      #La position du texte est légèrement décalée vers la droite, afin de mettre un espace entre les saisi
                            elif(NumeroRect == 2):      #Même principe pour les autres rectangles
                                screen.blit(saisi, [x2,y2])
                                nbObstacle += str(event.unicode)                        
                                x2+=20
                            elif(NumeroRect == 3):
                                screen.blit(saisi, [x3,y3])
                                nbMaxFourmis += str(event.unicode)
                                x3+=20
                            elif(NumeroRect == 4):
                                screen.blit(saisi, [x4,y4])
                                nbTourMaxMortSansManger += str(event.unicode)
                                x4+=20
                        except:  #Si il y a une erreur (donc que la saisie n'est pas un chiffre
                            screen.blit(erreur, [600,400])      #On affiche un message d'erreur
        
        #Ici, on affiche tous les textes qui ont été créé au début du programme
        screen.blit(image_fond, [100,20])
        screen.blit(Fois, [370,400])
        screen.blit(text_Start, [1010,850])
        screen.blit(nom_jeu, [475,25])
        screen.blit(param_taille, [25,400])
        screen.blit(param_nbObstacle, [25,500])
        screen.blit(param_nbMaxFourmis, [25,600])
        screen.blit(param_nbTourMaxMortSansManger, [25,700])
        screen.blit(param_posNourriture, [25,800])
        screen.blit(param_posNourriture1, [400,800])
        screen.blit(param_posNourriture2, [600,800])
        
        #Ligne très importante : le pygame.display.flip() permet d'actualiser la fenêtre
        pygame.display.flip()