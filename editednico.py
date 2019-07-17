# -*- coding: UTF-8 -*-


# Pygame-Modul importieren.

import pygame
import time
import os

# Überprüfen, ob die optionalen Text- und Sound-Module geladen werden konnten.



if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')

if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')




def buildWalls(playground):
    #Mauer oben
    playground[0][0] = 2
    playground[1][0] = 2
    playground[2][0] = 2
    playground[3][0] = 2
    playground[4][0] = 2
    playground[5][0] = 2
    playground[6][0] = 2
    playground[7][0] = 2
    playground[8][0] = 2
    playground[9][0] = 2
    playground[10][0] = 2
    playground[11][0] = 2
    playground[12][0] = 2
    playground[13][0] = 2
    playground[14][0] = 2
    playground[15][0] = 2
    playground[16][0] = 2
    playground[17][0] = 2
    playground[18][0] = 2
    playground[19][0] = 2
    #Mauer unten
    playground[0][9] = 2
    playground[1][9] = 2
    playground[2][9] = 2
    playground[3][9] = 2
    playground[4][9] = 2
    playground[5][9] = 2
    playground[6][9] = 2
    playground[7][9] = 2
    playground[8][9] = 2
    playground[9][9] = 2
    playground[10][9] = 2
    playground[11][9] = 2
    playground[12][9] = 2
    playground[13][9] = 2
    playground[14][9] = 2
    playground[15][9] = 2
    playground[16][9] = 2
    playground[17][9] = 2
    playground[18][9] = 2
    playground[19][9] = 2
    #Mauer links
    playground[0][1] = 2
    playground[0][2] = 2
    playground[0][4] = 2
    playground[0][5] = 2
    playground[0][6] = 2
    playground[0][7] = 2
    playground[0][8] = 2
    playground[0][9] = 2
    #Mauer rechts
    playground[19][1] = 2
    playground[19][2] = 2
    playground[19][4] = 2
    playground[19][5] = 2
    playground[19][6] = 2
    playground[19][7] = 2
    playground[19][8] = 2
    playground[19][9] = 2
    #Block 1
    playground[2][2] = 2
    playground[2][3] = 2
    playground[3][3] = 2
    #Block 2
    playground[2][5] = 2
    playground[2][6] = 2
    playground[2][7] = 2
    #Block 3
    playground[5][2] = 2
    playground[6][2] = 2
    playground[7][2] = 2
    playground[8][2] = 2
    playground[6][3] = 2
    #Block 4
    playground[4][7] = 2
    playground[5][6] = 2
    playground[5][7] = 2
    playground[6][5] = 2
    playground[6][6] = 2
    playground[6][7] = 2
    #Block 5
    playground[10][2] = 2
    playground[10][3] = 2
    #Block 6
    playground[8][6] = 2
    playground[10][6] = 2
    playground[8][7] = 2
    playground[9][7] = 2
    playground[10][7] = 2
    #Block 7
    playground[13][2] = 2
    playground[13][3] = 2
    playground[14][2] = 2
    playground[14][3] = 2
    #Block 8
    playground[12][5] = 2
    playground[12][6] = 2
    playground[12][7] = 2
    playground[13][6] = 2
    #Block 9
    playground[16][2] = 2
    #Block 10
    playground[16][4] = 2
    playground[16][7] = 2
    playground[17][4] = 2
    playground[17][5] = 2
    playground[17][6] = 2
    playground[17][7] = 2
    #Block 11
    playground[8][4] = 2
    

    pass

def main():
    # Initialisieren aller Pygame-Module und

    # Fenster erstellen (wir bekommen eine Surface, die den Bildschirm repräsentiert).

    pygame.init()
    pygame.display.set_caption("Frankas Pacman")

    #TODO: Load graphics
    pacman_img = pygame.image.load(os.path.join("", "pacmanmitmund.jpg"))
    pacman_img = pygame.transform.scale(pacman_img, (228, 50))


    size = 50
    sizePoints = 25

    x = int(1000 / size)
    y = int(500 / size)

    playground = []

    for i_x in range(0, x):
        playground.append([])
        for i_y in range(0, y):
            playground[i_x].append(3)

    buildWalls(playground)






    

    pacman_x = 9
    pacman_y = 6

    playground[pacman_x][pacman_y] = 1

    screen = pygame.display.set_mode((x*size, y*size))

    # Titel des Fensters setzen, Mauszeiger nicht verstecken und Tastendrücke wiederholt senden.

    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")

    pygame.mouse.set_visible(1)

    pygame.key.set_repeat(1, 30)

    # Clock-Objekt erstellen, das wir benötigen, um die Framerate zu begrenzen.

    clock = pygame.time.Clock()

    running = True
    clock.tick(60)
    tick = int(round(time.time() * 1000))

    mouthCounter = 0
    points = 0

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                #rechte Taste drücken, nach rechts gehen und Punkte sammeln
                if event.key == pygame.K_RIGHT and (int(round(time.time() * 1000)) - tick) > 100:
                    tick = int(round(time.time() * 1000))
                    if(pacman_x + 1 >= x):
                        playground[pacman_x][pacman_y] = 0
                        pacman_x = 0
                        playground[pacman_x][pacman_y] = 1

                    else:
                        # check for collision
                        if (playground[pacman_x + 1][pacman_y] != 2):
                            

                            playground[pacman_x][pacman_y] = 0
                            pacman_x = pacman_x + 1
                            playground[pacman_x][pacman_y] = 1
                            
                #linke Taste drücken, nach links gehen und Punkte sammeln
                if event.key == pygame.K_LEFT and (int(round(time.time() * 1000)) - tick) > 100:
                    tick = int(round(time.time() * 1000))
                    if(pacman_x == 0):
                        playground[pacman_x][pacman_y] = 0
                        pacman_x = x-1
                        playground[pacman_x][pacman_y] = 1

                    else:
                        # check for collision with wall und Punkte sammeln
                        if (playground[pacman_x -1][pacman_y] != 2):
                            

                            playground[pacman_x][pacman_y] = 0
                            pacman_x = pacman_x - 1
                            playground[pacman_x][pacman_y] = 1
                            
                #unten Taste drücken, nach unten gehen und Punkte sammeln
                if event.key == pygame.K_DOWN and (int(round(time.time() * 1000)) - tick) > 100:
                    tick = int(round(time.time() * 1000))
                    if(pacman_y + 1 >= y):
                        playground[pacman_x][pacman_y] = 0
                        pacman_y = 0
                        playground[pacman_x][pacman_y] = 1

                    else:
                        # check for collision with wall und Punkte sammeln
                        if (playground[pacman_x][pacman_y+1] != 2):
                            

                            playground[pacman_x][pacman_y] = 0
                            pacman_y = pacman_y + 1
                            playground[pacman_x][pacman_y] = 1

                #oben Taste drücken, nach oben gehen und Punkte sammeln            
                if event.key == pygame.K_UP and (int(round(time.time() * 1000)) - tick) > 100:
                    tick = int(round(time.time() * 1000))
                    if(pacman_y == 0):
                        playground[pacman_x][pacman_y] = 0
                        pacman_y = y-1
                        playground[pacman_x][pacman_y] = 1

                    else:
                        # check for collision with wall und Punkte sammeln
                        if (playground[pacman_x][pacman_y - 1] != 2):
                            

                            playground[pacman_x][pacman_y] = 0
                            pacman_y = pacman_y - 1
                            playground[pacman_x][pacman_y] = 1

                if playground[pacman_x][pacman_y] == 4:
                    running = False

                    print ("You lost")
                        



                

                    # 2+1 = anzBilder
                if (mouthCounter < 4):
                     mouthCounter = mouthCounter + 1
                else:
                     mouthCounter = 0


                
                

                #TODO: OBEN UND UNTEN






        #pygame.transform.scale()


        for i_x in range(0, x):
            for i_y in range(0, y):
                aktField = playground[i_x][i_y]
                #Empty Field
                if(aktField == 0):
                    pygame.draw.rect(screen, (255,255,255), [i_x*size,i_y*size, size, size], 0)

                #player
                if (aktField == 1):
                    pass

                #Wall
                if (aktField == 2):
                    pygame.draw.rect(screen, (0,0,255), [i_x*size,i_y*size, size, size], 0)

                #Point
                if (aktField == 3):
                    pygame.draw.rect(screen, (0,255,255), [i_x*size,i_y*size, size, size], 0)


        #Draw Pacman
        #                                pos_x, pos_y, höhe, länge
        screen.blit(pacman_img, (pacman_x*size, pacman_y*size), (size * mouthCounter, 0, size, size))


        # Inhalt von screen anzeigen.
        pygame.display.flip()


# Überprüfen, ob dieses Modul als Programm läuft und nicht in einem anderen Modul importiert wird.

if __name__ == '__main__':
    # Unsere Main-Funktion aufrufen.

    main()
