# On importe et initialise Pygame, les classes que l'on utilisera, et les modules de random
import pygame
from fourmi import Fourmi
from Obstacle import Obstacle
from nourriture import Nourriture
from random import *
import Menu_Accueil

pygame.init()

def fin_Simulation(tour, nourriture, fourmis):  #Cette fonction sert à afficher le menu de fin de simulation
    # On définit les variables suivantes comme globales, pour pouvoir les utiliser dans la fonction
    global screen, police_arial2_Normal, couleur_blanc, couleur_noir
    
    screen.fill(couleur_noir) #On met un fond noir
    screen.blit(police_arial2_Normal.render("La simulation est terminée", True, couleur_blanc), (100,200))  #Sur lequel on affiche notre texte
    screen.blit(police_arial2_Normal.render("Voici vos performances :", True, couleur_blanc), (100,300))
    screen.blit(police_arial2_Normal.render((str(tour) + " tours se sont déroulés"), True, couleur_blanc), (100,400))   #Qui prend en compte les paramètres qui lui sont données
    screen.blit(police_arial2_Normal.render((str(fourmis) + " fourmis sont nées"), True, couleur_blanc), (100,500))
    screen.blit(police_arial2_Normal.render((str(nourriture) + " unités de nourriture ont été ramassées"), True, couleur_blanc), (100,600))
    screen.blit(police_arial2_Normal.render("Souhaitez-vous recommencer une simulation ?", True, couleur_blanc), (100,700))
    screen.blit(police_arial2_Normal.render("Recommencer", True, couleur_blanc), (100,800)) 
    screen.blit(police_arial2_Normal.render("Quitter", True, couleur_blanc), (300,800))
    rectangle_Restart= (90, 800, 200, 50)
    rectangle_Quit= (290, 800, 200, 50)
    pygame.draw.rect(screen, couleur_blanc, rectangle_Restart, 2)
    pygame.draw.rect(screen, couleur_blanc, rectangle_Quit, 2)
    pygame.display.flip()   #On actualise l'écran afin d'afficher nos modifications
    
    Menu=True
    while(Menu==True):  #Tant qu'on est dans le menu
        for event in pygame.event.get():    #On récupère les évenements
            if event.type == pygame.QUIT:   #Si on appuie sur la croix
                pygame.quit()   #L'application se quitte
            elif event.type == pygame.MOUSEBUTTONDOWN:      #Si on fait un clic de souris                     
                if pygame.Rect(rectangle_Restart).collidepoint(event.pos):  #Et que la souris est positionnée dans le rectange correspondant à "Recommencer"
                    Menu_Accueil.menu() #On ouvre un menu d'accueil, afin de recommencer une simulation
                elif pygame.Rect(rectangle_Quit).collidepoint(event.pos):   #Si la souris est positionnée dans le rectange correspondant à "Quitter"
                    pygame.quit()   #Alors l'application se quitte

def placementNourritureDebut(taille, pas,PosNourriture):  # Cette fonction permet de placer la nourriture au lancement de la  simulation
    # On définit les variables suivantes comme globales, pour pouvoir les utiliser dans la fonction
    global listeNourriture, nourritureDebut

    print("La nourriture est positionnée de façon", PosNourriture, "comme demandé.")

    # On définit 3 variables, qui rendre dans l'algorithme (qui sera amélioré) de positionnement par défaut de la nourriture
    NourritureActuelle = 0
    XNourriture = 1.1
    YNourriture = 1.1

    while NourritureActuelle < nourritureDebut:  # Tant que notre variable NourritureActuelle n'est pas égale à la nourriture qu'il devrait y avoir au début
        if (PosNourriture == "Aleatoire"):  # On regarde si elle doit être positionnée par défaut ou aléatoirement
            nouvelle_Nourriture = Nourriture(randint(0, taille - 1) * pas, 120 + randint(0, taille - 1) * pas, pas,PosNourriture,("Nourriture" + str(NourritureActuelle)))  # On créé une nourriture
        else:
            nouvelle_Nourriture = Nourriture(int(taille / XNourriture) * pas, 120 + int(taille / YNourriture) * pas, pas, PosNourriture, ("Nourriture" + str(NourritureActuelle)))
        listeNourriture.append(nouvelle_Nourriture)  # Et on l'ajoute à une liste
        NourritureActuelle += 1  # On indique que la nourriture actuelle augmente de 1
    return listeNourriture  # que l'on return


def creationfourmi(numero, taille, pas,NBTourSansmanger):  # Lorsque l'on appelle cette fonction (qui permet de créer une fourmi)
    fourmi = Fourmi(taille, pas, NBTourSansmanger, ("fourmi" + str(numero)))  # On créé la fourmi
    print("La", fourmi.Nom, "est donc créée")
    return fourmi  # Et on la return


def creationNourriture(X, Y, num, taille, pas):  # Cette fonction permet de créer une nourriture après la mort d'une fourmi
    # On définit la variable suivante comme globale, pour pouvoir l'utiliser dans la fonction
    global listeAPlacer

    AjoutNourriture = Nourriture(X, Y, pas, "", ("Nourriture" + str(num)))  # On créer la nourriture, à la position de décès de la nourriture
    print("Une nourriture a donc été créée à ma position de décès")
    listeAPlacer.append(AjoutNourriture)  # On l'ajoute de la liste de nourriture à placer sur la grille

def placementObstacle(taille, pas, param_Obstacles):
    # On définit les variables suivantes comme globales, pour pouvoir les utiliser dans la fonction
    global listeObstacle
    
    nbObstacle =0
    while nbObstacle < param_Obstacles:
        nouvel_obstacle = Obstacle(randint(0, taille - 1) * pas, 120 + randint(0, taille - 1) * pas, pas, ("Obstacle"+str(nbObstacle)))
        listeObstacle.append(nouvel_obstacle)      
        nbObstacle+=1

def Sim_Fourmiliere(Taille, NBObstacle, NBMaxFourmis, NBTourSansManger,PosNourriture):  # Il s'agit du programme principal de la fourmilière
    # On définit les variables suivantes comme globales, pour pouvoir les utiliser dans toutes les fonctions
    global nourritureDansFourmiliere, nbFourmi, nourritureTotal, nourritureDebut, placeNourritureDebut, listeNourriture, listeAPlacer, listeFourmi, listeObstacle, Simulation_Running, screen, couleur_noir, couleur_blanc, police_arial2_Normal
    
    print("Le programme débute")

    # On définit quelques couleurs, une police, des rectangles
    couleur_noir = (0, 0, 0)
    couleur_blanc = (255, 255, 255)
    couleur_fond = (61, 121, 42)
    police_arial = pygame.font.SysFont("arial", 50)
    police_arial2_Gras = pygame.font.SysFont("arial", 20, True)
    police_arial2_Normal = pygame.font.SysFont("arial", 20, )
    rectangle_Pas_a_pas= (600, 70, 275, 30)
    rectangle_Automatique= (600, 30, 275, 30)
    
    # On définit l'écran et une horloge interne à pygame
    clock = pygame.time.Clock()
    Ecran = (850, 970)
    screen = pygame.display.set_mode((Ecran))
    
    # On définit une variable qui permettent de créer la grille
    Pas = float(Ecran[0] / float(Taille))    
    
    # On définit des variables
    nourritureDansFourmiliere = int(int(Taille) / 2)  # Au début de la simulation, il y a déja un certain nombre de nourriture dans la fourmilière (pour faire naître les premières fourmis)
    turn = 0
    nourritureTotal = 0
    nourritureDebut = int(int(Taille) / 1.5)  # Correspond à la nourriture qui devra être créé au début de la simulation, elle dépend de la taille
    placeNourritureDebut = False  # La nourriture n'a pas encore été placée
    listeNourriture = []
    listeAPlacer = []
    listeFourmi = []
    placeObstacle=False
    listeObstacle = []
    NBTourSansManger = int(NBTourSansManger)    
    fourmiChercheuse = Fourmi(int(Taille), Pas, NBTourSansManger, "fourmiChercheuse")   #On créé la fourmi chercheuse
    listeFourmi.append(fourmiChercheuse)   #On l'ajoute à la liste des fourmis
    nbFourmi = 1 #Etant donné qu'on a créé la fourmi chercheuse, il y a déja une fourmi
    nbTotalFourmis = 1
    nbTourSansFourmis =0 #Cette variable correspond au nombre de tours pendant lesquels uniquement la fourmi chercheuse est vivante (elle sert à mettre fin à la simulation)
    pas_a_pas=False #Pour l'instant, la simulation n'est pas en mode pas à pas

    # On lance la simulation
    while True:
        clock.tick(int(nbFourmi*2))  # On explique qu'il y aura 30 images par secondes

        # On gère l'affichage de l'écran et de la fourmilière
        screen.fill(couleur_fond)
        fourmiliere_OK = pygame.transform.scale(pygame.image.load("asset/nest.png"), (int(Pas), int(Pas)))
        if (int(Taille) % 2 == 0):  
            screen.blit(fourmiliere_OK, [float(int(Taille) / 2 * Pas), float(120 + int(Taille) / 2 * Pas)])
        else:
            screen.blit(fourmiliere_OK,[float((int(Taille) + 1) / 2 * Pas), float(120 + ((int(Taille) + 1) / 2 * Pas))])
        
        # On dessine la grille
        xLigne = 0.0
        yLigne = 120.0
        while xLigne < Ecran[0]:  # Tant que la position x des lignes n'est pas égale à l'abscisse maximum de l'application
            pygame.draw.line(screen, couleur_noir, (xLigne, 0), (xLigne, Ecran[1]))  # Une ligne verticale est tracée
            xLigne += Pas  # Et la prochaine sera décalée
        while yLigne < Ecran[1]:  # Tant que la position y des lignes n'est pas égale à l'ordonnée maximum de l'application
            pygame.draw.line(screen, couleur_noir, (0, yLigne), (Ecran[0], yLigne))  # Une ligne horizontale est tracée
            yLigne += Pas  # Et la prochaine sera décalée
        
        # On place la nourriture
        if (placeNourritureDebut == False):  # Si la nourriture n'a pas encore été placée
                listeAPlacer = placementNourritureDebut(int(Taille), Pas, PosNourriture)  # Alors la liste ListeAPlacer prend la valeur du retour de la fonction placeNourritureDebut
                nourritureTotal = nourritureDebut
                placeNourritureDebut = True  # On indique que la nourriture a bien été placée
                
        #On place les obstacles
        if(placeObstacle == False):
            placementObstacle(int(Taille), Pas, int(NBObstacle))
            placeObstacle= True
        
        # Création des fourmis
        if (nbFourmi * 2 < nourritureDansFourmiliere and int(NBMaxFourmis) > nbFourmi):  # Gère la création des fourmis en fonction des conditions du cahier des charges et du paramétrage
            print("Il y a", nbFourmi, "fourmis, et", nourritureDansFourmiliere, "nourritures")
            listeFourmi.append(creationfourmi(nbTotalFourmis, int(Taille), Pas, NBTourSansManger))
            nbFourmi += 1
            nbTotalFourmis += 1
            nourritureDansFourmiliere -= 1
        
        # Déplacement et affichage fourmi
        for laFourmi in listeFourmi:  # Pour chaque fourmi
            if (laFourmi.Faim > 0 and laFourmi.TourMaxRestant > 0 and laFourmi.vie == True):  # On vérifie qu'elle est toujours apte à vivre
                Deplacement=False
                while(Deplacement==False):
                    Direction = randint(0, 7)  # On obtient un chiffre aléatoire entre 0 et 7
                    Depla=0
                    if (Direction == 0):  # Selon ce chiffre, la fourmi va se déplacer dans une direction (en lançant une fonction de sa classe)
                        for obstacle in listeObstacle:  
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x+Pas),laFourmi.rect.y) == True or laFourmi.rect.x+Pas >= Ecran[0]):  
                                Depla+=1    #On prévoit le déplacement avant de le faire. Si la fourmi se dirige sur un obstacle ou hors de la grille, la variable Depla s'incrémente
                        if(Depla==0):   #Or, pour que le déplacement se fasse, il faut que Depla soit égal à 0. Sinon, on recommence la boucle jusqu'à trouver un déplacement possible
                            laFourmi.MoveRight(Pas) #Si dépla est égal à 0, on appelle la fonction de déplacement de la fourmi
                            Deplacement=True    #et on sort de la boucle                             
                    elif (Direction == 1):    
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x-Pas),laFourmi.rect.y) == True or laFourmi.rect.x-Pas < 0):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveLeft(Pas)
                            Deplacement=True
                    elif (Direction == 2):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint(laFourmi.rect.x,(laFourmi.rect.y-Pas)) == True or laFourmi.rect.y-Pas < 120):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveTop(Pas)
                            Deplacement=True
                    elif (Direction == 3):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint(laFourmi.rect.x,(laFourmi.rect.y+Pas)) == True or laFourmi.rect.y+Pas >= Ecran[1]):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveDown(Pas)
                            Deplacement=True
                    elif (Direction == 4):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x+Pas),(laFourmi.rect.y-Pas)) == True or laFourmi.rect.x+Pas >= Ecran[0] or laFourmi.rect.y-Pas < 120):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveRight(Pas)
                            laFourmi.MoveTop(Pas)
                            Deplacement=True
                    elif (Direction == 5):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x+Pas),(laFourmi.rect.y+Pas)) == True or laFourmi.rect.x+Pas >= Ecran[0] or laFourmi.rect.y+Pas >= Ecran[1]):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveRight(Pas)
                            laFourmi.MoveDown(Pas)
                            Deplacement=True
                    elif (Direction == 6):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x-Pas),(laFourmi.rect.y-Pas)) == True or laFourmi.rect.x-Pas < 0 or laFourmi.rect.y-Pas < 120):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveLeft(Pas)
                            laFourmi.MoveTop(Pas)
                            Deplacement=True
                    elif (Direction == 7):
                        for obstacle in listeObstacle:
                            if(pygame.Rect(obstacle.rect).collidepoint((laFourmi.rect.x-Pas),(laFourmi.rect.y+Pas)) == True or laFourmi.rect.x-Pas > 0 or laFourmi.rect.y+Pas >= Ecran[1]):
                                Depla+=1
                        if(Depla==0):
                            laFourmi.MoveLeft(Pas)
                            laFourmi.MoveDown(Pas)
                            Deplacement=True
                if laFourmi.Nom != "fourmiChercheuse":      #Si la fourmi n'est pas la fourmi chercheuse
                    laFourmi.Faim -= 1  # Après s'être déplacée, une fourmi perd une unité de nourriture
                    laFourmi.TourMaxRestant -= 1  # Après s'être déplacé, son nombre de tour maximum restant diminue de 1
                #Cela ne s'applique pas à la fourmi chercheuse car elle est immortelle

                if (laFourmi.Faim > 0):  # Si malgré ça elle n'a toujours pas 0 nourriture, alors on l'affiche
                    screen.blit(laFourmi.image, laFourmi.rect)

            if ((laFourmi.Faim <= 0 or laFourmi.TourMaxRestant <= 0) and laFourmi.vie == True):  # Si une fourmi n'a plus de nourriture et qu'elle est en vie
                nbFourmi -= 1  # On enregistre qu'il y a une fourmi en moins
                laFourmi.vie = False  # On l'indique comme morte, pour ne plus avoir à la traiter
                print("Je suis", laFourmi.Nom, "et je suis morte")
                nourritureTotal += 1  # On indique que le nombre de nourriture total augmente de 1
                creationNourriture(laFourmi.rect.x, laFourmi.rect.y, nourritureTotal, int(Taille),Pas)  # Car on créé une nourriture à la position de décès de notre fourmi
                laFourmi.Faim -= 1  # Ligne à supprimer ???
                laFourmi.TourMaxRestant -= 1  # Ligne à supprimer ???

            for laNourriture in listeAPlacer:  # Pour chaque nourriture que l'on doit placer
                if (pygame.Rect(laNourriture.rect).collidepoint(laFourmi.rect.x,laFourmi.rect.y) and laNourriture.mange == False and laFourmi.vie == True):  # Si elle est en contact avec une fourmi et qu'elle n'a pas déja été mangée
                    laNourriture.mange = True  # Alors on indique qu'elle est mangée
                    nourritureDansFourmiliere += 1  # La nourriture de la fourmilière augmente de 1 (normalement c'est pas ça, mais c'est une première version
                    laFourmi.Faim = 20  # La faim de la fourmi vaut 20 : elle s'est nourrie
                    print("Je suis la", laFourmi.Nom, "et j'ai mangé la", laNourriture.Nom)
                    
        if pas_a_pas == True and turn > 0: #Si le pas à pas est activé et qu'un tour a déja été réalisé
                    tour_suivant=False  
                    while tour_suivant==False:  #On lance une boucle afin de figer le programme
                        for event in pygame.event.get():    #On récupère les évenements
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #Si on appuie sur la barre espace
                                tour_suivant = True     #On passe au tour suivant
                            if event.type == pygame.QUIT:  # Si on clique sur la croix
                                screen.fill(couleur_noir)   #On met un fond noir
                                pygame.quit()  #Puis la simulation s'arrête
                            elif event.type == pygame.MOUSEBUTTONDOWN:      #Si on fait un clic de souris                      
                                if pygame.Rect(rectangle_Pas_a_pas).collidepoint(event.pos):    #Sur "pas à pas"
                                    pas_a_pas=True  #On reste en pas à pas, aucune modification
                                if pygame.Rect(rectangle_Automatique).collidepoint(event.pos):  #Sur "automatique"
                                    pas_a_pas=False     #On n'est plus en pas à pas (donc par déduction on est en automatique)
                                    tour_suivant=True       #Et on sort de la boucle
        #Petite note : Si certains évènements tels que pygame.quit() sont présents à la fois dans la boucle précédente, c'est parce que lorsque nous sommes en pas à pas
        #Nous sommes bloqués à l'intérieur de cette boucle. Nous n'avons donc pas accès aux autres évènements qui ne s'y trouve pas. Il serait donc impossible de quitter le programme
                                    
        for laNourriture in listeAPlacer:  # Pour chaque nourriture que l'on peut placer
            if laNourriture.mange == False:  # Si la nourriture n'a pas déja été mangée
                screen.blit(laNourriture.image, laNourriture.rect)  # Alors on l'affiche
        
        for obstacle in listeObstacle:  #On affiche chacun des obstacles
            screen.blit(obstacle.image, obstacle.rect)

        for event in pygame.event.get():  # Pour chacun des évènement récupérés par Pygame
            if event.type == pygame.QUIT:  # Si on clique sur la croix
                screen.fill(couleur_noir)
                pygame.quit()  # Alors la simulation s'arrête
            elif event.type == pygame.MOUSEBUTTONDOWN:      #Si on fait un clic de souris                      
                if pygame.Rect(rectangle_Pas_a_pas).collidepoint(event.pos):
                    pas_a_pas = True
                if pygame.Rect(rectangle_Automatique).collidepoint(event.pos):
                    pas_a_pas=False
                
        if nbFourmi == 1:   #Si il n'y a qu'une seule fourmi en vie (c'est à dier la fourmi chercheuse
            nbTourSansFourmis += 1  #Alors on incrémente cette variable

        if nbTourSansFourmis == 5:  # Si le tour pendant lesquels uniquement la fourmi chercheuse est vivante est égal à 5
            nourritureMange=0   
            for nourriture in listeNourriture:  #On compte le nombre de nourriture qui ont été mangés
                if nourriture.mange==True:
                    nourritureMange +=1
            fin_Simulation(turn, nourritureMange, nbTotalFourmis)  # Alors on lance le menu de fin  (en lui renseignant le nombre total de tours, de nourritures mangées, et de fourmis)

        # HEADER, ici on gère tous les éléments graphiques du bandeau
        turn = turn + 1
        imagefour = pygame.image.load("asset/fourmi.png")
        rectfour = imagefour.get_rect()
        rectfour.x = 500
        rectfour.y = 20

        imagenourr = pygame.image.load("asset/Nourriture.png")
        imagenourr = pygame.transform.scale(imagenourr, (50, 50))
        rectnourr = imagefour.get_rect()
        rectnourr.x = 500
        rectnourr.y = 20

        imageturn = pygame.image.load("asset/time.png")
        imageturn = pygame.transform.scale(imageturn, (50, 50))
        rectturn = imageturn.get_rect()
        rectturn.x = 500
        rectturn.y = 20

        pygame.draw.rect(screen, (191, 191, 191), (0, 0, 1200, 120))  # Ajoute la barre
        
        if pas_a_pas == True:   
            screen.blit(police_arial2_Normal.render("Automatique", True, couleur_noir), (610,35))
            screen.blit(police_arial2_Gras.render("Pas à pas (barre espace)", True, couleur_noir), (610,75))
        else:
            screen.blit(police_arial2_Gras.render("Automatique", True, couleur_noir), (610,35))
            screen.blit(police_arial2_Normal.render("Pas à pas (barre espace)", True, couleur_noir), (610,75))
        
        pygame.draw.rect(screen, couleur_noir, rectangle_Automatique, 2)
        pygame.draw.rect(screen, couleur_noir, rectangle_Pas_a_pas, 2)
        
        screen.blit(imagefour, (240, 35))  # Ajout indicateur Fourmis
        screen.blit(imagenourr, (0, 35))  # Ajout indicateur Nourriture dans la fourmilliere
        screen.blit(imageturn,(400,35))
        
        AffichageNbTurn = police_arial.render(str(turn),True,couleur_noir)
        AffichageNbFourmi = police_arial.render(str(nbFourmi), True, couleur_noir)
        nbNourriture = police_arial.render(str(nourritureDansFourmiliere), True, couleur_noir)

        screen.blit(AffichageNbTurn , [450, 30])
        screen.blit(AffichageNbFourmi, [300, 30])
        screen.blit(nbNourriture, [50, 30])

        pygame.display.flip()   #A la fin de chaque boucle, on actualise le programme afin d'afficher les modifications
