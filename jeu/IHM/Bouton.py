import core


class Bouton:
    def __init__(self,coordX,coordY, Visible=True):  # constructeur
        self.visible = Visible
        self.couleur = (255,255,255)
        self.position = (coordX, coordY)
        self.mass = 20

    def show(self):
        if self.visible:
            core.Draw.circle(self.couleur, self.position, self.mass)
