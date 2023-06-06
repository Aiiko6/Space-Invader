import pygame

from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageOption:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.bp = Bouton1(300, 200,Etat.SKIN)
        self.bp1 = Bouton1(300, 300,Etat.GRAPHI)
        self.bp2 = Bouton1(300, 400,Etat.MENU)
        self.massCursor = 2

    def update(self):

        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Option :', (300, 10))
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Skin ', (340, 180))
        self.bp1.show()
        self.bp1.update()
        core.Draw.text(self.couleur, 'Graphisme ', (340, 280))
        self.bp2.show()
        self.bp2.update()
        core.Draw.text(self.couleur, 'Retour ', (340, 380))
