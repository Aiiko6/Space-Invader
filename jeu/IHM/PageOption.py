import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageOption:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.bp = Bouton(300, 200)
        self.bp1 = Bouton(300, 300)
        self.bp2 = Bouton(300, 400)
        self.bp3 = Bouton(300, 500)
        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1

    def update(self):

        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Option :', (300, 10))
        self.bp.show()
        core.Draw.text(self.couleur, 'Skin ', (340, 180))
        self.bp1.show()
        core.Draw.text(self.couleur, 'Graphisme ', (340, 280))
        self.bp2.show()
        core.Draw.text(self.couleur, 'Retour ', (340, 380))

        if (self.startMenu == 0) or (not core.getMouseLeftClick()):
            self.startMenu = 0
            if core.getMouseLeftClick() and self.distanceCheck(self.bp):
                self.startMenu = 1
                core.memory('etat', Etat.SKIN)
            if core.getMouseLeftClick() and self.distanceCheck(self.bp1):
                self.startMenu = 1
                core.memory('etat', Etat.GRAPHI)
            if core.getMouseLeftClick() and self.distanceCheck(self.bp2):
                self.startMenu = 1
                core.memory('etat', Etat.MENU)

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False
