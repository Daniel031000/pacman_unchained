#This Collision Detection uses simple rectangle collision Boxes
import math

def checkForCollisionBetweenObjects(obj1, obj2):
    #check if there is collision between 2 objects
    obj1Top = obj1.position[1] -1
    obj1Bottom = obj1.position[1] + obj1.hitBox[1] +1
    obj1Left = obj1.position[0] -1
    obj1Right = obj1.position[0] + obj1.hitBox[0] +1

    obj2Top = obj2.position[1]
    obj2Bottom = obj2.position[1] + obj2.hitBox[1]
    obj2Left = obj2.position[0]
    obj2Right = obj2.position[0] + obj2.hitBox[0]

    #Check where object 1 collides
    hitBottom = obj1Bottom > obj2Top
    hitTop = obj1Top < obj2Bottom
    hitLeft = obj1Left < obj2Right
    hitRight = obj1Right > obj2Left
    

    if hitBottom and hitTop and hitLeft and hitRight:
        #got hit
        hitDirection = "Bottom"
        #check if below or above
        if obj1Top < obj2Bottom and obj1Bottom < obj2Bottom:
            #obj1 is above obj2
            if obj1Left < obj2Right and obj1Right > obj2Right:
                #is on Right Site (Left Collision)
                if math.fabs(obj1Left - obj2Right) > math.fabs(obj1Bottom - obj2Top):
                    #is Bottom
                    return "Bottom"
                else:
                    #is LEFT
                    return "Left"
            else:
                #is on Left Site (Right Collision)
                if math.fabs(obj1Right - obj2Left) > math.fabs(obj1Bottom - obj2Top):
                    #is Bottom
                    return "Bottom"
                else:
                    #is RIGHT
                    return "Right"
        else:
            #obj1 is below obj2
            if obj1Left < obj2Right and obj1Right > obj2Right:
                #is on Right Site (Left Collision)
                if math.fabs(obj1Left - obj2Right) > math.fabs(obj1Top - obj2Bottom):
                    #is TOP
                    return "Top"
                else:
                    #is LEFT
                    return "Left"
            else:
                #is on Left Site (Right Collision)
                if math.fabs(obj1Right - obj2Left) > math.fabs(obj1Top - obj2Bottom):
                    #is TOP
                    return "Top"
                else:
                    #is RIGHT
                    return "Right"
            
    else:
        return "None"
