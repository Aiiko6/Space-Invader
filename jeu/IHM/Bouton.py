import core


class Bouton:
    def __init__(self,coordX,coordY):  # constructeur
        self.couleur = (255,255,255)
        self.position = (coordX, coordY)
        self.mass = 20

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.mass)
