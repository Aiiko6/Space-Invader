from jeu import core


class Vaisseau:
    def __init__(self):  # constructeur
        self.speed = 10
        self.position = (100, 535)
        self.mass = 20


    def show(self):

        if not core.memory("TextureVaisseau").ready:
            core.memory("TextureVaisseau").load()
        core.memory("TextureVaisseau").pos = (self.position[0] - 25, self.position[1] - 25)
        core.memory("TextureVaisseau").show()

    def deplacement(self):  # Deplacmement du vaisseau suivant les touches pressé
        if core.getKeyPressList("d") and self.position[0] < 775:
            self.position = (self.position[0] + self.speed, self.position[1])
        if core.getKeyPressList("q") and self.position[0] > 25:
            self.position = (self.position[0] + -self.speed, self.position[1])

    def getPosX(self):
        return self.position[0]