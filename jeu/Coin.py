from pygame import Vector2

import core


class Coin:
    def __init__(self,coordX, coordY):
        self.position = Vector2(coordX,coordY)
        self.vitesse = 4
        self.gain = 1
        self.mass = 12
        self.color = (255,255,255)

        core.memory("textureCoins", core.Texture("./Image/Coins.png", self.position, 0, (30, 24)))

    def update(self):
        self.position[1] = self.position[1] + self.vitesse

        if not core.memory("textureCoins").ready:
            core.memory("textureCoins").load()
        core.memory("textureCoins").pos = (self.position[0] - 15,self.position[1] - 12)
        core.memory("textureCoins").show()

        if self.position[1] > core.WINDOW_SIZE[1]:
            return True

    def collisionJoueur(self, Vaisseau):
        pos1 = Vector2(self.position)
        pos2 = Vector2(Vaisseau.position)
        distance = pos1 - pos2
        if self.mass + Vaisseau.mass > distance.length():
            return True


