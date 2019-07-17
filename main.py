import pygame
import sys

import globalVariables as gV
import player as p
import Matrix
gameRunning = True



pygame.init()

pygame.display.set_caption("PacMan von Daniel Khadra")

clock = pygame.time.Clock()

gameObjects = []

player = p.player("Chris")
gameObjects.append(player)

while gameRunning:

    for gO in gameObjects:
        gO.update()

    #Get pygameEvents
    gV.pyEvents = pygame.event.get()

    #Check Basic Events
    for event in gV.pyEvents:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Draw
    gameWindow.fill((255, 255, 255))
    gameWindow.blit(gameBackground, gameBackground.get_rect())
    #Draw GameObjects
    for gO in gameObjects:
        Bild.blit(gO.imgToDraw(), (gO.pos[0] - (gO.imgToDraw().get_rect().size[0] / 2), gO.pos[1] - (gO.imgToDraw().get_rect().size[1] / 2)))

    #Update Pygame Screen
    pygame.display.update()

    #Check For Game End
    if player.pos[0] > 650 and player.pos[1] < 150:
        pygame.quit()
        sys.exit()

    #Set 30 fps
    clock.tick(30) # 30 fps
    
