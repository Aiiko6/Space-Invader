from pygame import Vector2

from jeu import core


class Fire:
    def __init__(self,coordX, coordY):
        self.position = Vector2(coordX,coordY)
        self.vitesse = 4
        self.gain = 1
        self.mass = 12

        self.timeToLive = 0
        core.memory("textureFire", core.Texture("./Image/Fire.gif", self.position, 0, (50, 50)))

        self.son = core.Sound("./Sound/tnt.mp3", 2)
        self.bRunOnce = False

    def update(self):
        if self.bRunOnce == False:

            self.bRunOnce = True

        self.timeToLive = self.timeToLive + 1
        self.position[1] = self.position[1]
        core.memory("textureFire").setScalesize((2 + self.timeToLive) * 10, (2 + self.timeToLive) * 10)

        core.memory("textureFire").load()
        core.memory("textureFire").show()

        if self.position[1] > core.WINDOW_SIZE[1]:
            return True

    def getTimeToLive(self):
        return self.timeToLive

