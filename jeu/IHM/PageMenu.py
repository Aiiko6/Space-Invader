import core
from jeu.IHM.Bouton import Bouton


class PageMenu:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton(300,200)
        self.bp1 = Bouton(300, 300)


    def update(self):
        core.Draw.text(self.couleur, 'Space invader: ', (300, 10))
        self.bp.show()
        core.Draw.text(self.couleur, 'Jouer ', (340, 180))
        self.bp1.show()
        core.Draw.text(self.couleur, 'Parametres ', (340, 280))
        