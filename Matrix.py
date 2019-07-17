import sys
import pygame
import math
import time
import ani
import globalVariables as gV
import player as p
gameRunning = True
pygame.display.set_caption("PacMan von Daniel Khadra")
#Erstellen einer Matrix/Spielfelds

def BauL1(Spielfeld): #Spielfeld von Level 1
    #ObereWand
    Spielfeld[0][0] = 1
    Spielfeld[1][0] = 1
    Spielfeld[2][0] = 1
    Spielfeld[3][0] = 1
    Spielfeld[4][0] = 1
    Spielfeld[5][0] = 1
    Spielfeld[6][0] = 1
    Spielfeld[7][0] = 1
    Spielfeld[8][0] = 1
    Spielfeld[9][0] = 1
    Spielfeld[10][0] = 1
    Spielfeld[11][0] = 1
    Spielfeld[12][0] = 1
    Spielfeld[13][0] = 1
    Spielfeld[14][0] = 1
    Spielfeld[15][0] = 1
    Spielfeld[16][0] = 1
    Spielfeld[17][0] = 1
    Spielfeld[18][0] = 1
    Spielfeld[19][0] = 1
    Spielfeld[20][0] = 1
    Spielfeld[21][0] = 1
    Spielfeld[22][0] = 1
    Spielfeld[23][0] = 1
    Spielfeld[24][0] = 1
    Spielfeld[25][0] = 1
    Spielfeld[26][0] = 1
    Spielfeld[27][0] = 1
    Spielfeld[28][0] = 1
    Spielfeld[29][0] = 1
    Spielfeld[30][0] = 1
    Spielfeld[31][0] = 1
    Spielfeld[32][0] = 1
    Spielfeld[33][0] = 1
    Spielfeld[34][0] = 1
    Spielfeld[35][0] = 1
    Spielfeld[36][0] = 1
    Spielfeld[37][0] = 1
    Spielfeld[38][0] = 1
    Spielfeld[39][0] = 1
#Spielfeld Rand Unten
    Spielfeld[0][19] = 1
    Spielfeld[1][19] = 1
    Spielfeld[2][19] = 1
    Spielfeld[3][19] = 1
    Spielfeld[4][19] = 1
    Spielfeld[5][19] = 1
    Spielfeld[6][19] = 1
    Spielfeld[7][19] = 1
    Spielfeld[8][19] = 1
    Spielfeld[9][19] = 1
    Spielfeld[10][19] = 1
    Spielfeld[11][19] = 1
    Spielfeld[12][19] = 1
    Spielfeld[13][19] = 1
    Spielfeld[14][19] = 1
    Spielfeld[15][19] = 1
    Spielfeld[16][19] = 1
    Spielfeld[17][19] = 1
    Spielfeld[18][19] = 1
    Spielfeld[19][19] = 1
    Spielfeld[20][19] = 1
    Spielfeld[21][19] = 1
    Spielfeld[22][19] = 1
    Spielfeld[23][19] = 1
    Spielfeld[24][19] = 1
    Spielfeld[25][19] = 1
    Spielfeld[26][19] = 1
    Spielfeld[27][19] = 1
    Spielfeld[28][19] = 1
    Spielfeld[29][19] = 1
    Spielfeld[30][19] = 1
    Spielfeld[31][19] = 1
    Spielfeld[32][19] = 1
    Spielfeld[33][19] = 1
    Spielfeld[34][19] = 1
    Spielfeld[35][19] = 1
    Spielfeld[36][19] = 1
    Spielfeld[37][19] = 1
    Spielfeld[38][19] = 1
    Spielfeld[39][19] = 1
#Spielfeld Rand Links
    Spielfeld[0][0] = 1
    Spielfeld[0][1] = 1
    Spielfeld[0][2] = 1
    Spielfeld[0][3] = 1
    Spielfeld[0][4] = 1
    Spielfeld[0][5] = 1
    Spielfeld[0][6] = 1
    Spielfeld[0][7] = 1
    Spielfeld[0][8] = 1
    Spielfeld[0][10] = 1
    Spielfeld[0][11] = 1
    Spielfeld[0][12] = 1
    Spielfeld[0][13] = 1
    Spielfeld[0][14] = 1
    Spielfeld[0][15] = 1
    Spielfeld[0][16] = 1
    Spielfeld[0][17] = 1
    Spielfeld[0][18] = 1
    Spielfeld[0][19] = 1
#Spielfeld Rand Rechts
    Spielfeld[39][0] = 1
    Spielfeld[39][1] = 1
    Spielfeld[39][2] = 1
    Spielfeld[39][3] = 1
    Spielfeld[39][4] = 1
    Spielfeld[39][5] = 1
    Spielfeld[39][6] = 1
    Spielfeld[39][7] = 1
    Spielfeld[39][8] = 1
    Spielfeld[39][10] = 1
    Spielfeld[39][11] = 1
    Spielfeld[39][12] = 1
    Spielfeld[39][13] = 1
    Spielfeld[39][14] = 1
    Spielfeld[39][15] = 1
    Spielfeld[39][16] = 1
    Spielfeld[39][17] = 1
    Spielfeld[39][18] = 1
    Spielfeld[39][19] = 1
#InneresLevel1 (nach jeder y Koordinate aufgeteilt)
    Spielfeld[19][1] = 1
    Spielfeld[20][1] = 1
    Spielfeld[2][2] = 1
    Spielfeld[3][2] = 1
    Spielfeld[4][2] = 1
    Spielfeld[5][2] = 1
    Spielfeld[6][2] = 1
    Spielfeld[8][2] = 1
    Spielfeld[9][2] = 1
    Spielfeld[10][2] = 1
    Spielfeld[12][2] = 1
    Spielfeld[13][2] = 1
    Spielfeld[14][2] = 1
    Spielfeld[16][2] = 1
    Spielfeld[17][2] = 1
    Spielfeld[19][2] = 1
    Spielfeld[20][2] = 1
    Spielfeld[22][2] = 1
    Spielfeld[23][2] = 1
    Spielfeld[25][2] = 1
    Spielfeld[26][2] = 1
    Spielfeld[27][2] = 1
    Spielfeld[29][2] = 1
    Spielfeld[30][2] = 1
    Spielfeld[31][2] = 1
    Spielfeld[33][2] = 1
    Spielfeld[34][2] = 1
    Spielfeld[35][2] = 1
    Spielfeld[36][2] = 1
    Spielfeld[37][2] = 1
    Spielfeld[2][3] = 1
    Spielfeld[3][3] = 1
    Spielfeld[4][3] = 1
    Spielfeld[5][3] = 1
    Spielfeld[6][3] = 1
    Spielfeld[8][3] = 1
    Spielfeld[14][3] = 1
    Spielfeld[16][3] = 1
    Spielfeld[17][3] = 1
    Spielfeld[19][3] = 1
    Spielfeld[20][3] = 1
    Spielfeld[22][3] = 1
    Spielfeld[23][3] = 1
    Spielfeld[25][3] = 1
    Spielfeld[31][3] = 1
    Spielfeld[33][3] = 1
    Spielfeld[34][3] = 1
    Spielfeld[35][3] = 1
    Spielfeld[36][3] = 1
    Spielfeld[37][3] = 1
    Spielfeld[8][4] = 1
    Spielfeld[10][4] = 1
    Spielfeld[11][4] = 1
    Spielfeld[12][4] = 1
    Spielfeld[14][4] = 1
    Spielfeld[16][4] = 1
    Spielfeld[17][4] = 1
    Spielfeld[22][4] = 1
    Spielfeld[23][4] = 1
    Spielfeld[25][4] = 1
    Spielfeld[27][4] = 1
    Spielfeld[28][4] = 1
    Spielfeld[29][4] = 1
    Spielfeld[31][4] = 1
    Spielfeld[2][5] = 1
    Spielfeld[3][5] = 1
    Spielfeld[4][5] = 1
    Spielfeld[5][5] = 1
    Spielfeld[6][5] = 1
    Spielfeld[10][5] = 1
    Spielfeld[11][5] = 1
    Spielfeld[12][5] = 1
    Spielfeld[16][5] = 1
    Spielfeld[17][5] = 1
    Spielfeld[19][5] = 1
    Spielfeld[20][5] = 1
    Spielfeld[22][5] = 1
    Spielfeld[23][5] = 1
    Spielfeld[27][5] = 1
    Spielfeld[28][5] = 1
    Spielfeld[29][5] = 1
    Spielfeld[33][5] = 1
    Spielfeld[34][5] = 1
    Spielfeld[35][5] = 1
    Spielfeld[36][5] = 1
    Spielfeld[37][5] = 1
    Spielfeld[2][6] = 1
    Spielfeld[3][6] = 1
    Spielfeld[4][6] = 1
    Spielfeld[5][6] = 1
    Spielfeld[6][6] = 1
    Spielfeld[16][6] = 1
    Spielfeld[17][6] = 1
    Spielfeld[19][6] = 1
    Spielfeld[20][6] = 1
    Spielfeld[22][6] = 1
    Spielfeld[23][6] = 1
    Spielfeld[33][6] = 1
    Spielfeld[34][6] = 1
    Spielfeld[35][6] = 1
    Spielfeld[36][6] = 1
    Spielfeld[37][6] = 1
    Spielfeld[8][6] = 1
    Spielfeld[14][6] = 1
    Spielfeld[25][6] = 1
    Spielfeld[31][6] = 1
    Spielfeld[8][7] = 1
    Spielfeld[9][7] = 1
    Spielfeld[10][7] = 1
    Spielfeld[12][7] = 1
    Spielfeld[13][7] = 1
    Spielfeld[14][7] = 1
    Spielfeld[16][7] = 1
    Spielfeld[17][7] = 1
    Spielfeld[19][7] = 1
    Spielfeld[20][7] = 1
    Spielfeld[22][7] = 1
    Spielfeld[23][7] = 1
    Spielfeld[25][7] = 1
    Spielfeld[26][7] = 1
    Spielfeld[27][7] = 1
    Spielfeld[29][7] = 1
    Spielfeld[30][7] = 1
    Spielfeld[31][7] = 1
    Spielfeld[1][8] = 1
    Spielfeld[2][8] = 1
    Spielfeld[3][8] = 1
    Spielfeld[4][8] = 1
    Spielfeld[5][8] = 1
    Spielfeld[34][8] = 1
    Spielfeld[35][8] = 1
    Spielfeld[36][8] = 1
    Spielfeld[37][8] = 1
    Spielfeld[38][8] = 1
    Spielfeld[7][9] = 1
    Spielfeld[8][9] = 1
    Spielfeld[9][9] = 1
    Spielfeld[10][9] = 1
    Spielfeld[11][9] = 1
    Spielfeld[12][9] = 1
    Spielfeld[14][9] = 1
    Spielfeld[15][9] = 1
    Spielfeld[16][9] = 1
    Spielfeld[17][9] = 1
    Spielfeld[18][9] = 1
    Spielfeld[19][9] = 1
    Spielfeld[20][9] = 1
    Spielfeld[21][9] = 1
    Spielfeld[22][9] = 1
    Spielfeld[23][9] = 1
    Spielfeld[24][9] = 1
    Spielfeld[25][9] = 1
    Spielfeld[27][9] = 1
    Spielfeld[28][9] = 1
    Spielfeld[29][9] = 1
    Spielfeld[30][9] = 1
    Spielfeld[31][9] = 1
    Spielfeld[32][9] = 1
    Spielfeld[1][10] = 1
    Spielfeld[2][10] = 1
    Spielfeld[3][10] = 1
    Spielfeld[4][10] = 1
    Spielfeld[5][10] = 1
    Spielfeld[34][10] = 1
    Spielfeld[35][10] = 1
    Spielfeld[36][10] = 1
    Spielfeld[37][10] = 1
    Spielfeld[38][10] = 1
    Spielfeld[8][11] = 1
    Spielfeld[9][11] = 1
    Spielfeld[10][11] = 1
    Spielfeld[12][11] = 1
    Spielfeld[13][11] = 1
    Spielfeld[14][11] = 1
    Spielfeld[16][11] = 1
    Spielfeld[17][11] = 1
    Spielfeld[19][11] = 1
    Spielfeld[20][11] = 1
    Spielfeld[22][11] = 1
    Spielfeld[23][11] = 1
    Spielfeld[25][11] = 1
    Spielfeld[26][11] = 1
    Spielfeld[27][11] = 1
    Spielfeld[29][11] = 1
    Spielfeld[30][11] = 1
    Spielfeld[31][11] = 1
    Spielfeld[2][12] = 1
    Spielfeld[3][12] = 1
    Spielfeld[4][12] = 1
    Spielfeld[5][12] = 1
    Spielfeld[6][12] = 1
    Spielfeld[8][12] = 1
    Spielfeld[14][12] = 1
    Spielfeld[16][12] = 1
    Spielfeld[17][12] = 1
    Spielfeld[19][12] = 1
    Spielfeld[20][12] = 1
    Spielfeld[22][12] = 1
    Spielfeld[23][12] = 1
    Spielfeld[25][12] = 1
    Spielfeld[31][12] = 1
    Spielfeld[33][12] = 1
    Spielfeld[34][12] = 1
    Spielfeld[35][12] = 1
    Spielfeld[36][12] = 1
    Spielfeld[37][12] = 1
    Spielfeld[2][13] = 1
    Spielfeld[3][13] = 1
    Spielfeld[4][13] = 1
    Spielfeld[5][13] = 1
    Spielfeld[6][13] = 1
    Spielfeld[8][13] = 1
    Spielfeld[10][13] = 1
    Spielfeld[11][13] = 1
    Spielfeld[12][13] = 1
    Spielfeld[14][12] = 1
    Spielfeld[16][13] = 1
    Spielfeld[17][13] = 1
    Spielfeld[19][13] = 1
    Spielfeld[20][13] = 1
    Spielfeld[22][13] = 1
    Spielfeld[23][13] = 1
    Spielfeld[25][13] = 1
    Spielfeld[27][13] = 1
    Spielfeld[28][13] = 1
    Spielfeld[29][13] = 1
    Spielfeld[31][13] = 1
    Spielfeld[33][13] = 1
    Spielfeld[34][13] = 1
    Spielfeld[35][13] = 1
    Spielfeld[36][13] = 1
    Spielfeld[37][13] = 1
    Spielfeld[10][14] = 1
    Spielfeld[11][14] = 1
    Spielfeld[12][14] = 1
    Spielfeld[16][14] = 1
    Spielfeld[17][14] = 1
    Spielfeld[19][14] = 1
    Spielfeld[20][14] = 1
    Spielfeld[22][14] = 1
    Spielfeld[23][14] = 1
    Spielfeld[27][14] = 1
    Spielfeld[28][14] = 1
    Spielfeld[29][14] = 1
    Spielfeld[2][15] = 1
    Spielfeld[3][15] = 1
    Spielfeld[4][15] = 1
    Spielfeld[5][15] = 1
    Spielfeld[6][15] = 1
    Spielfeld[8][15] = 1
    Spielfeld[10][15] = 1
    Spielfeld[11][15] = 1
    Spielfeld[12][15] = 1
    Spielfeld[14][15] = 1
    Spielfeld[16][15] = 1
    Spielfeld[17][15] = 1
    Spielfeld[22][15] = 1
    Spielfeld[23][15] = 1
    Spielfeld[25][15] = 1
    Spielfeld[27][15] = 1
    Spielfeld[28][15] = 1
    Spielfeld[29][15] = 1
    Spielfeld[31][15] = 1
    Spielfeld[33][15] = 1
    Spielfeld[34][15] = 1
    Spielfeld[35][15] = 1
    Spielfeld[36][15] = 1
    Spielfeld[37][15] = 1
    Spielfeld[2][16] = 1
    Spielfeld[3][16] = 1
    Spielfeld[4][16] = 1
    Spielfeld[5][16] = 1
    Spielfeld[6][16] = 1
    Spielfeld[8][16] = 1
    Spielfeld[14][16] = 1
    Spielfeld[16][16] = 1
    Spielfeld[17][16] = 1
    Spielfeld[19][16] = 1
    Spielfeld[20][16] = 1
    Spielfeld[22][16] = 1
    Spielfeld[23][16] = 1
    Spielfeld[25][16] = 1
    Spielfeld[31][16] = 1
    Spielfeld[33][16] = 1
    Spielfeld[34][16] = 1
    Spielfeld[35][16] = 1
    Spielfeld[36][16] = 1
    Spielfeld[37][16] = 1
    Spielfeld[2][17] = 1
    Spielfeld[3][17] = 1
    Spielfeld[4][17] = 1
    Spielfeld[5][17] = 1
    Spielfeld[6][17] = 1
    Spielfeld[8][17] = 1
    Spielfeld[9][17] = 1
    Spielfeld[10][17] = 1
    Spielfeld[12][17] = 1
    Spielfeld[13][17] = 1
    Spielfeld[14][17] = 1
    Spielfeld[16][17] = 1
    Spielfeld[17][17] = 1
    Spielfeld[19][17] = 1
    Spielfeld[20][17] = 1
    Spielfeld[22][17] = 1
    Spielfeld[23][17] = 1
    Spielfeld[25][17] = 1
    Spielfeld[26][17] = 1
    Spielfeld[27][17] = 1
    Spielfeld[29][17] = 1
    Spielfeld[30][17] = 1
    Spielfeld[31][17] = 1
    Spielfeld[33][17] = 1
    Spielfeld[34][17] = 1
    Spielfeld[35][17] = 1
    Spielfeld[36][17] = 1
    Spielfeld[37][17] = 1
    Spielfeld[19][19] = 1
    Spielfeld[20][19] = 1
    pass 




    



def Matrix():
        Größe = 25
        Spielfeld=[]
        x = int(1000/Größe)
        y = int(500/Größe)
        for i_x in range(0, x):
                Spielfeld.append([])
                for i_y in range(0, y):
                    Spielfeld[i_x].append(3)
        BauL1(Spielfeld)
        Bild = pygame.display.set_mode((x*Größe, y*Größe))
        pacman_x = 9
        pacman_y = 6
        Spielfeld[pacman_x][pacman_y] = 2

            
        for i_x in range(0, x):
            for i_y in range(0, y):
                aktField = Spielfeld[i_x][i_y]
                #Empty Field
                if(aktField == 0):
                    pygame.draw.rect(Bild, (0,0,0), [i_x*Größe,i_y*Größe, Größe, Größe], 0)

                #player
                if (aktField == 2):
                    pass

                #Wall
                if (aktField == 1):
                    pygame.draw.rect(Bild, (0,0,255), [i_x*Größe,i_y*Größe, Größe, Größe], 0)
                #einzelne Punkte einfügen 
                if (aktField == 3):
                    pygame.draw.rect(Bild, (255,201,41), [i_x*Größe,i_y*Größe, Größe, Größe], 0)

      
        pygame.key.set_repeat(1, 30)
        
        pygame.init()
        clock = pygame.time.Clock()

        gameObjects = []

        player = p.player("Daniel")
        gameObjects.append(player)
        mouthCounter=0

        while gameRunning:

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
Matrix()    
pygame.display.flip()

