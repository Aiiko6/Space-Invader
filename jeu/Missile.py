from jeu import core


class Missile:
    def __init__(self, coordX, Vitesse):  # constructeur
        self.vitesse = Vitesse
        self.position = (coordX, 550)
        self.mass = 5
        self.alive = False

        core.memory("textureMissile", core.Texture("./Image/Missile.png", self.position, 0, (8, 15)))

    def show(self):
        if not core.memory("textureMissile").ready:
            core.memory("textureMissile").load()
        core.memory("textureMissile").pos = self.position
        core.memory("textureMissile").show()

    def deplacementMissile(self, X):
        self.position = (X - 4, 550)

    def trajectoire(self):
        if (self.position[0] > 0) and (self.position[0] < 800):
            self.position = (self.position[0], self.position[1] + (self.vitesse * -1))

    def collision(self):
        # Si dépassement de l'écran
        if self.position[1] < 0:
            return True

    def isAlive(self):
        return self.alive
