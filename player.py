import pygame
import ani
import globalVariables as gV

pacman_x = 9
pacmany_y = 6

class player: #PacMan als Klasse definieren
    def __init__(self, name):
        self.name = name
        self.pos = [235, 160] #Startposition
        self.movementDirection = [0, 0] #eigene Bewegung 
        self.movementSpeed = 5 #der Speed in dem er sich bewegt sobald ein event gestartet wird
        #einzelne Animationen aus den Ordnern  
        self.currentAnimationType = "Idle" #nur am Start nötig
        # input is a string and a tuple that contains the properties
        self.playerSpriteIdle = ani.MySprite("character_Player_Idle", ("Player/Idle",))
        self.playerSpriteWalkHori = ani.MySprite("spriteSheet_Player_Hori", ("Player/WalkHori", 5, 1, 0, 0, 4))
        self.playerSpriteWalkUp = ani.MySprite("character_Player_Up", ("Player/WalkUp", 5, 1, 0, 0, 4))
        self.playerSpriteWalkDown = ani.MySprite("character_Player_Down", ("Player/WalkDown", 5, 1, 0, 0, 4))

        self.animationSlowDown = 5
        self.animationSlowDownCounter = 0
    # Bewegung des Packmans
    # Waits for a key event and performs an action if up/w, down/s, left/a or right/d is triggered
    def doMove(self):
        for event in gV.pyEvents:
             if event.type == pygame.KEYDOWN:
                 if event.key in (pygame.K_LEFT, pygame.K_a):
                     self.movementDirection[0] = -1
                     self.currentAnimationType = "Walk"
                     self.movementDirection[1] = 0 #Damit er nicht diagonal läuft
                     '''if(pacman_x == 0):
                         Spielfeld[pacman_x][pacman_y] = 0
                         pacman_x = x-1
                         Spielfeld[pacman_x][pacman_y] = 1
                     else:
                         # check for collision with wall und Punkte sammeln
                         if (Spielfeld[pacman_x -1][pacman_y] != 2):
                             Spielfeld[pacman_x][pacman_y] = 0
                             pacman_x = pacman_x - 1
                             Spielfeld[pacman_x][pacman_y] = 1'''
                 elif event.key in (pygame.K_RIGHT, pygame.K_d):
                     self.movementDirection[0] = 1
                     self.currentAnimationType = "Walk"
                     self.movementDirection[1] = 0
                     '''if(pacman_x + 1 >= x):
                         Spielfeld[pacman_x][pacman_y] = 0
                         pacman_x = 0
                         Spielfeld[pacman_x][pacman_y] = 1
                     else:
                         # check for collision
                         if (Spielfeld[pacman_x + 1][pacman_y] != 2):
                             Spielfeld[pacman_x][pacman_y] = 0
                             pacman_x = pacman_x + 1
                             Spielfeld[pacman_x][pacman_y] = 1'''
                 elif event.key in (pygame.K_UP, pygame.K_w):
                     self.movementDirection[1] = -1
                     self.currentAnimationType = "Walk"
                     self.movementDirection[0] = 0
                     '''if(pacman_y == 0):
                         Spielfeld[pacman_x][pacman_y] = 0
                         pacman_y = y-1
                         Spielfeld[pacman_x][pacman_y] = 1
                     else: 
                         # check for collision with wall und Punkte sammeln
                         if (Spielfeld[pacman_x][pacman_y - 1] != 2):  
                             Spielfeld[pacman_x][pacman_y] = 0
                             pacman_y = pacman_y - 1
                             Spielfeld[pacman_x][pacman_y] = 1'''
                 elif event.key in (pygame.K_DOWN, pygame.K_s):
                     self.movementDirection[1] = 1
                     self.currentAnimationType = "Walk"
                     self.movementDirection[0] = 0
                     '''if(pacman_y + 1 >= y):
                         Spielfeld[pacman_x][pacman_y] = 0
                         pacman_y = 0
                         Spielfeld[pacman_x][pacman_y] = 1
                     else:
                         # check for collision with wall und Punkte sammeln
                         if (Spielfeld[pacman_x][pacman_y+1] != 2):
                             Spielfeld[pacman_x][pacman_y] = 0
                             pacman_y = pacman_y + 1
                             Spielfeld[pacman_x][pacman_y] = 1'''


        self.pos = [x + y for x, y in zip(self.pos, [i * self.movementSpeed for i in self.movementDirection]  )]

    def update(self):
        #Movement
        self.doMove()
        
        #Set Animation Idle
        if self.movementDirection[0] == 0 and self.movementDirection[1] == 0:
            self.currentAnimationType = "Idle"

        #Updating Animations
        #Perform Every X Frames
        if self.animationSlowDownCounter < self.animationSlowDown:
            self.animationSlowDownCounter += 1
        else:
            self.updateAnimationSprites()
            self.animationSlowDownCounter = 0

        #Draw Character
        self.imgToDraw()

    def imgToDraw(self):        
        if self.currentAnimationType == "Idle": #printen der einzelnen Animatione je nach"Walk" oder "Idle"
            imageToBeDrawn = self.playerSpriteIdle.image
            self.playerSpriteIdle.update()
            return imageToBeDrawn
        elif self.currentAnimationType == "Walk":
            if self.movementDirection[1] == -1:
                imageToBeDrawn = self.playerSpriteWalkUp.image
                return imageToBeDrawn
            elif self.movementDirection[1] == 1:
                imageToBeDrawn = self.playerSpriteWalkDown.image
                return imageToBeDrawn
            elif self.movementDirection[0] == -1:
                imageToBeDrawn = pygame.transform.flip(self.playerSpriteWalkHori.image, True, False)
                return imageToBeDrawn
            elif self.movementDirection[0] == 1:
                imageToBeDrawn = self.playerSpriteWalkHori.image
                return imageToBeDrawn
            else:
                print("Exeption 1")
                imageToBeDrawn = self.playerSpriteIdle.image
                return imageToBeDrawn
        else:
            print("Exeption 2")
            imageToBeDrawn = self.playerSpriteIdle.image
            return imageToBeDrawn

    def updateAnimationSprites(self):
        if self.currentAnimationType == "Idle": #damit sich nicht mehrere Animations überschneiden
            self.playerSpriteIdle.update()
            self.playerSpriteWalkHori.reset()
            self.playerSpriteWalkUp.reset()
            self.playerSpriteWalkDown.reset()
        elif self.currentAnimationType == "Walk":
            if self.movementDirection[1] == -1:
                self.playerSpriteWalkUp.update()
                self.playerSpriteIdle.reset()
                self.playerSpriteWalkHori.reset()
                self.playerSpriteWalkDown.reset()
            elif self.movementDirection[1] == 1:
                self.playerSpriteWalkDown.update()
                self.playerSpriteIdle.reset()
                self.playerSpriteWalkHori.reset()
                self.playerSpriteWalkUp.reset()
            elif self.movementDirection[0] == -1 or self.movementDirection[0] == 1:
                self.playerSpriteWalkHori.update()
                self.playerSpriteIdle.reset()
                self.playerSpriteWalkUp.reset()
                self.playerSpriteWalkDown.reset()
            
