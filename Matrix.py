import sys
import pygame
import math
import time
import ani
import globalVariables as gV
import player as p
import spielfeldLevel1

gameRunning = True
pygame.display.set_caption("PacMan von Daniel Khadra")


##########################
# Erstellen einer Matrix/Spielfelds
##########################


# nimmt die Positionseigenschaften einer Wandeinheit und
# generiert eine Liste, die weitere Listen enthaelt mit jeweils 2 Elementen
# Dabei ist das erste Element die x-Koordinate und das zweite die y-Koordinate


def main():
        # Größe eines kleinsten Quadrates
        gV.Größe = 25

        x = int(1000/gV.Größe)  # = 40
        y = int(500/gV.Größe)  # = 20

        # fill Spielfeld 2d array with 3
        for i_x in range(0, x):
                gV.Spielfeld.append([])
                for i_y in range(0, y):
                    gV.Spielfeld[i_x].append(3)
        # print(Spielfeld)
        spielfeldLevel1.BauL1(gV.Spielfeld)
        # display size = (1000, 500)
        Bild = pygame.display.set_mode((x*Größe, y*Größe))
        pacman_x = 9
        pacman_y = 6
        # Pacman Anfangsposition = 2
        gV.Spielfeld[pacman_x][pacman_y] = 2

        # checks the
        for i_x in range(0, x):
            for i_y in range(0, y):
                aktField = gV.Spielfeld[i_x][i_y]
                #Empty Field
                if(aktField == 0):
                    pygame.draw.rect(Bild, (0,0,0), [i_x*gV.Größe,i_y*gV.Größe, gV.Größe, gV.Größe], 0)
                #player
                if (aktField == 2):
                    pass
                #Wall
                if (aktField == 1):
                    pygame.draw.rect(Bild, (0,0,255), [i_x*gV.Größe,i_y*gV.Größe, gV.Größe, gV.Größe], 0)
                #einzelne Punkte einfügen
                if (aktField == 3):
                    pygame.draw.rect(Bild, (255,201,41), [i_x*gV.Größe,i_y*gV.Größe, gV.Größe, gV.Größe], 0)

        for x in range (1000):
            pixelRow=[]
            for y in range (500):
                pixelRow.append(pygame.display.get_surface().get_at((x,y)))
            gV.pixelColours.append(pixelRow)
        print(gV.pixelColours)
        pygame.key.set_repeat(1, 30)

        pygame.init()
        clock = pygame.time.Clock()

        gameObjects = []

        player = p.player("Daniel")
        gameObjects.append(player)
        mouthCounter = 0


        # TODO: gameRunning is always True anyway?
        while gameRunning:
            gV.playerPosition=player.pos
            for gO in gameObjects:
                gO.update()

            #Get pygameEvents
            gV.pyEvents = pygame.event.get()

            #Damit es einfach geschlossen werden kann
            for event in gV.pyEvents:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #Draw GameObjects
            for gO in gameObjects:
                Bild.blit(gO.imgToDraw(), (gO.pos[0] - (gO.imgToDraw().get_rect().size[0] / 2), gO.pos[1] - (gO.imgToDraw().get_rect().size[1] / 2)))

            #Update Pygame Screen
            pygame.display.update()

            if (mouthCounter < 4):
                mouthCounter = mouthCounter + 1
            else:
                mouthCounter = 0
            #Set 30 fps
            clock.tick(30) # 32 fps


main()
pygame.display.flip()



