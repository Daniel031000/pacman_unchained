class gamePlatform:

    name = "platform"
    objType = "Platform"

    position = [0, 0]
    hitBox = [50, 50] #Default

    def __init__(self, startPos, hitBox):
        self.position = startPos
        self.hitBox = hitBox

##########################
#Enemy der zufällig läuft#
##########################
import random
class Geist:
    def Grundstock(self):
        self.movementDirection=[0,0]
        self.movementSpeed=5
    def Moving(self):
        while gameRunning:
        self.movementDirection[random(0,1)] = random(-1,1)
        if self.movementDirection[0]== -1:
            self.movementDirection[1]=0
        elif self.movementDirection[0]==1:
            self.movementDirection[1] = 0
        else:
            self.movementDirection[1] = random(-1, 1)
            self.movementDirection[0] = 0
     def Image00(self):
