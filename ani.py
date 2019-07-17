import pygame
import sys
import os

imageFolder = "Graphics"

def getAnimationFromFolder(fileName, folderName):
    animationFromImages = []
    for filename in os.listdir(imageFolder + "/" + folderName):
        print(filename)
        if fileName in filename:
            animationFromImages.append(pygame.image.load(imageFolder + "/" + folderName + "/" + filename))
    return animationFromImages

def getAnimationFromSpritesheet(sheetName, folderName, numberOfHorizontalSprites, numberOfVerticalSprites, horizontalStart, verticalStart, numberOfImages):
    print(sheetName)
    print(folderName)
    spriteSheet = pygame.image.load(imageFolder + "/" + folderName + "/" + sheetName + ".png")
    spriteSheetSize = spriteSheet.get_size()
    spriteSingleSize = (spriteSheetSize[0]/numberOfHorizontalSprites, spriteSheetSize[1]/numberOfVerticalSprites)
    animationFromSpriteSheet = []
    x = horizontalStart
    y = verticalStart
    for nOI in range(numberOfImages):
        animationSprite = pygame.Surface((spriteSingleSize[0], spriteSingleSize[1]))
        animationSprite.blit(spriteSheet, (0, 0), (x*spriteSingleSize[0], y*spriteSingleSize[1], spriteSingleSize[0], spriteSingleSize[1]))
        animationSprite = animationSprite.convert()
        colorkey = animationSprite.get_at((0,0))
        animationSprite.set_colorkey(colorkey, pygame.RLEACCEL)
        
        animationFromSpriteSheet.append(animationSprite)
        x += 1
        if x > numberOfHorizontalSprites - 1:
            y += 1
            x = 0

    return animationFromSpriteSheet


class MySprite(pygame.sprite.Sprite):
    def __init__(self, spriteName, properties): #horSprites, vertSprites, horStart, vertStart, numberOfImages
        self.images = []
        print(len(properties))
        print(properties)
        if len(properties) == 1:
            self.images = getAnimationFromFolder(spriteName, properties[0])
        else:
            self.images = getAnimationFromSpritesheet(spriteName, properties[0], properties[1], properties[2], properties[3], properties[4], properties[5])
        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def reset(self):
        self.index = 0

