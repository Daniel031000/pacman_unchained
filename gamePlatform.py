class gamePlatform:

    name = "platform"
    objType = "Platform"

    position = [0, 0]
    hitBox = [50, 50] #Default

    def __init__(self, startPos, hitBox):
        self.position = startPos
        self.hitBox = hitBox
