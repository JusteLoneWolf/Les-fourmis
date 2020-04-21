# On importe et initialise Pygame, les classes que l'on utilisera, et les modules de random
import pygame
from fourmi import Fourmi
from nourriture import Nourriture
from random import *

pygame.init()


def Next(
        choix):  # Cette fonction est lancée depuis Menu_Accueil, elle permet de savoir si l'on doit accéder à la simulation
    global Simulation_Running
    Simulation_Running = choix


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
            nouvelle_Nourriture = Nourriture(randint(0, taille - 1) * pas, 120 + randint(0, taille - 1) * pas, pas,
                                             PosNourriture,
                                             ("Nourriture" + str(NourritureActuelle)))  # On créé une nourriture
        else:
            nouvelle_Nourriture = Nourriture(int(taille / XNourriture) * pas, 120 + int(taille / YNourriture) * pas,
                                             pas, PosNourriture, ("Nourriture" + str(NourritureActuelle)))

        listeNourriture.append(nouvelle_Nourriture)  # Et on l'ajoute à une liste
        NourritureActuelle += 1  # On indique que la nourriture actuelle augmente de 1
    return listeNourriture  # que l'on return


def creationfourmi(numero, taille, pas,
                   NBTourSansmanger):  # Lorsque l'on appelle cette fonction (qui permet de créer une fourmi)
    fourmi = Fourmi(taille, pas, NBTourSansmanger, ("fourmi" + str(numero)))  # On créé la fourmi
    print("La", fourmi.Nom, "est donc créée")
    return fourmi  # Et on la return


def creationNourriture(X, Y, num, taille,
                       pas):  # Cette fonction permet de créer une nourriture après la mort d'une fourmi
    # On définit la variable suivante comme globale, pour pouvoir l'utiliser dans la fonction
    global listeAPlacer

    AjoutNourriture = Nourriture(X, Y, pas, "", (
            "Nourriture" + str(num)))  # On créer la nourriture, à la position de décès de la nourriture
    print("Une nourriture a donc été créée à ma position de décès")
    listeAPlacer.append(AjoutNourriture)  # On l'ajoute de la liste de nourriture à placer sur la grille


def Sim_Fourmiliere(Taille, NBObstacle, NBMaxFourmis, NBTourSansManger,
                    PosNourriture):  # Il s'agit du programme principal de la fourmilière
    # On définit les variables suivantes comme globales, pour pouvoir les utiliser dans toutes les fonctions
    global nourritureDansFourmiliere, nbFourmi, nourritureTotal, nourritureDebut, placeNourritureDebut, listeNourriture, listeAPlacer, listeFourmi, Simulation_Running

    print("Le programme débute")

    # On définit quelques couleurs, une police et une image
    couleur_noir = (0, 0, 0)
    couleur_blanc = (255, 255, 255)
    couleur_fond = (61, 121, 42)
    police_arial = pygame.font.SysFont("arial", 50)
    # fourmiliere = pygame.image.load("image2.png")

    # On définit l'écran et une horloge interne à pygame
    clock = pygame.time.Clock()
    Ecran = (850, 970)
    screen = pygame.display.set_mode((Ecran))

    # On définit des variable
    nourritureDansFourmiliere = int(int(
        Taille) / 2)  # Au début de la simulation, il y a déja un certain nombre de nourriture dans la fourmilière (pour faire naître les premières fourmis)
    nbFourmi = 0
    turn = 0
    nbTotalFourmis = 0
    nourritureTotal = 0
    nourritureDebut = int(int(
        Taille) / 1.5)  # Correspond à la nourriture qui devra être créé au début de la simulation, elle dépend de la taille
    placeNourritureDebut = False  # La nourriture n'a pas encore été placée
    listeNourriture = []
    listeAPlacer = []
    listeFourmi = []
    NBTourSansManger = int(NBTourSansManger)
    # On définit les variables qui permettent de créer la grille
    Pas = float(Ecran[0] / float(Taille))

    # On lance la simulation
    while True:
        # On gère l'affichage de l'écran et de la fourmilière
        screen.fill(couleur_fond)
        fourmiliere_OK = pygame.transform.scale(pygame.image.load("asset/nest.png"), (int(Pas), int(Pas)))
        if (int(Taille) % 2 == 0):
            screen.blit(fourmiliere_OK, [float(int(Taille) / 2 * Pas), float(120 + int(Taille) / 2 * Pas)])
        else:
            screen.blit(fourmiliere_OK,
                        [float((int(Taille) + 1) / 2 * Pas), float(120 + ((int(Taille) + 1) / 2 * Pas))])

        # On dessine la grille
        xLigne = 0.0
        yLigne = 120.0
        while xLigne < Ecran[
            0]:  # Tant que la position x des lignes n'est pas égale à l'abscisse maximum de l'application
            pygame.draw.line(screen, couleur_noir, (xLigne, 0), (xLigne, Ecran[1]))  # Une ligne verticale est tracée
            xLigne += Pas  # Et la prochaine sera décalée
        while yLigne < Ecran[
            1]:  # Tant que la position y des lignes n'est pas égale à l'ordonnée maximum de l'application
            pygame.draw.line(screen, couleur_noir, (0, yLigne), (Ecran[0], yLigne))  # Une ligne horizontale est tracée
            yLigne += Pas  # Et la prochaine sera décalée

            # On place les frites
            if (placeNourritureDebut == False):  # Si la nourriture n'a pas encore été placée
                listeAPlacer = placementNourritureDebut(int(Taille), Pas,
                                                        PosNourriture)  # Alors la liste ListeAPlacer prend la valeur du retour de la fonction placeNourritureDebut
                nourritureTotal = nourritureDebut
                placeNourritureDebut = True  # On indique que la nourriture a bien été placée

        # Création des fourmis
        if (nbFourmi * 2 < nourritureDansFourmiliere and int(
                NBMaxFourmis) > nbFourmi):  # Gère la création des fourmis en fonction des conditions du cahier des charges et du paramétrage
            print("Il y a", nbFourmi, "fourmis, et", nourritureDansFourmiliere, "nourritures")
            listeFourmi.append(creationfourmi(nbTotalFourmis, int(Taille), Pas, NBTourSansManger))
            nbFourmi += 1
            nbTotalFourmis += 1
            nourritureDansFourmiliere -= 1

        # Déplacement et affichage fourmi
        for laFourmi in listeFourmi:  # Pour chaque fourmi
            if (
                    laFourmi.Faim > 0 and laFourmi.TourMaxRestant > 0 and laFourmi.vie == True):  # On vérifie qu'elle est toujours apte à vivre
                clock.tick(30)  # On explique qu'il y aura 30 images par secondes
                Direction = randint(0, 7)  # On obtient un chiffre aléatoire entre 0 et 7
                if (
                        Direction == 0):  # Selon ce chiffre, la fourmi va se déplacer dans une direction (en lançant une fonction de sa classe
                    laFourmi.MoveRight(Pas)
                elif (Direction == 1):
                    laFourmi.MoveLeft(Pas)
                elif (Direction == 2):
                    laFourmi.MoveTop(Pas)
                elif (Direction == 3):
                    laFourmi.MoveDown(Pas)
                elif (Direction == 4):
                    laFourmi.MoveRight(Pas)
                    laFourmi.MoveTop(Pas)
                elif (Direction == 5):
                    laFourmi.MoveRight(Pas)
                    laFourmi.MoveDown(Pas)
                elif (Direction == 6):
                    laFourmi.MoveLeft(Pas)
                    laFourmi.MoveTop(Pas)
                elif (Direction == 7):
                    laFourmi.MoveLeft(Pas)
                    laFourmi.MoveDown(Pas)
                laFourmi.Faim -= 1  # Après s'être déplacée, une fourmi perd une unité de nourriture
                laFourmi.TourMaxRestant -= 1  # Après s'être déplacé, son nombre de tour maximum restant diminue de 1
                if (laFourmi.Faim > 0):  # Si malgré ça elle n'a toujours pas 0 nourriture, alors on l'affiche
                    screen.blit(laFourmi.image, laFourmi.rect)

            if ((
                    laFourmi.Faim <= 0 or laFourmi.TourMaxRestant <= 0) and laFourmi.vie == True):  # Si une fourmi n'a plus de nourriture et qu'elle est en vie
                nbFourmi -= 1  # On enregistre qu'il y a une fourmi en moins
                laFourmi.vie = False  # On l'indique comme morte, pour ne plus avoir à la traiter
                print("Je suis", laFourmi.Nom, "et je suis morte")
                nourritureTotal += 1  # On indique que le nombre de nourriture total augmente de 1
                creationNourriture(laFourmi.rect.x, laFourmi.rect.y, nourritureTotal, int(Taille),
                                   Pas)  # Car on créé une nourriture à la position de décès de notre fourmi
                laFourmi.Faim -= 1  # Ligne à supprimer ???
                laFourmi.TourMaxRestant -= 1  # Ligne à supprimer ???

            for laNourriture in listeAPlacer:  # Pour chaque nourriture que l'on doit placer
                if (pygame.Rect(laNourriture.rect).collidepoint(laFourmi.rect.x,
                                                                laFourmi.rect.y) and laNourriture.mange == False and laFourmi.vie == True):  # Si elle est en contact avec une fourmi et qu'elle n'a pas déja été mangée
                    laNourriture.mange = True  # Alors on indique qu'elle est mangée
                    nourritureDansFourmiliere += 1  # La nourriture de la fourmilière augmente de 1 (normalement c'est pas ça, mais c'est une première version
                    laFourmi.Faim = 20  # La faim de la fourmi vaut 20 : elle s'est nourrie
                    print("Je suis la", laFourmi.Nom, "et j'ai mangé la", laNourriture.Nom)

        for laNourriture in listeAPlacer:  # Pour chaque nourriture que l'on peut placer
            if laNourriture.mange == False:  # Si la nourriture n'a pas déja été mangée
                screen.blit(laNourriture.image, laNourriture.rect)  # Alors on l'affiche

        for event in pygame.event.get():  # Pour chacun des évènement récupérés par Pygame
            if event.type == pygame.QUIT:  # Si on clique sur la croix
                screen.fill(couleur_noir)
                pygame.quit()  # Alors la simulation s'arrête


        if nbFourmi == 0:  # Si le nombre de fourmi est égal à 0
            pygame.quit()  # Alors on arrête la simulation

        # HEADER
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

        screen.blit(imagefour, (440, 35))  # Ajout indicateur Fourmis
        screen.blit(imagenourr, (0, 35))  # Ajout indicateur Nourriture dans la fourmilliere
        screen.blit(imageturn,(700,35))

        AffichageNbTurn = police_arial.render(str(turn),True,couleur_noir)
        AffichageNbFourmi = police_arial.render(str(nbFourmi), True, couleur_noir)
        nbNourriture = police_arial.render(str(nourritureDansFourmiliere), True, couleur_noir)

        screen.blit(AffichageNbTurn , [750, 30])
        screen.blit(AffichageNbFourmi, [500, 30])
        screen.blit(nbNourriture, [50, 30])

        pygame.display.flip()
