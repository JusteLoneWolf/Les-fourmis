import pygame  # Installation "pip install pygame" avec la derniere version de python
import sys
from Class.Game import Game  # Appel de la class Game

pygame.init()  # Initialisation

pygame.display.set_caption('Les fourmis')  # Nomme le jeu
screen = pygame.display.set_mode((1280, 720))  # Forme la fenetre

background = pygame.image.load('asset/back/back.png')  # Met le fond
game = Game()  # Met la class Game() dans game pour que ca face plus joli dans le code <3

# Bloucle infini
run = True  # Le jeu tourne ( ͡° ͜ʖ ͡°)z

while run:  # "Moteur"
    screen.blit(background, (0, -200))  # Met le back
    screen.blit(game.player.playerImage, game.player.rect)  # Met le joueurerbas

    if game.press.get(
            pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():  # si la touche
                                                                                                     # fleche droite est appyer j'avance si je cogne la bordure je m'arrete
        game.player.move_r()
    elif game.press.get(pygame.K_LEFT) and game.player.rect.x > 0:  # si la touche fleche gauche est appyer j'avance
        game.player.move_l()
    elif game.press.get(pygame.K_UP) and game.player.rect.y > 0:  # si la touche fleche haut est appyer j'avance
        game.player.move_u()
    elif game.press.get(
            pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():  # si la touche
                                                                                                     # fleche droite est appyer j'avance si je cogne la bordure je m'arrete
        game.player.move_d()

    pygame.display.flip()  # Mise a jours ecran

    for event in pygame.event.get():  # Get les event
        if event.type == pygame.QUIT:  # Si l'event quit est lance je ferme le jeu
            run = False  # Le jeux ne tourne pas  (ಥ﹏ಥ)
            pygame.quit()  # Fermeture du jeux
            print('Fermeture... ')  # Envoi en console
            sys.exit(0)  # ferme le programme


        elif event.type == pygame.KEYDOWN:  # Si une touche est appuyer
            game.press[event.key] = True  # Je prend le numeros de la touche et je dit qu'elle est vrai pour qu'elle puisse
                                   # execute (va avec le code un peux plus en haut)
        elif event.type == pygame.KEYUP:  # Si une touche est relache
            game.press[event.key] = False  # Je met la touche en false pour arreter l'execution
