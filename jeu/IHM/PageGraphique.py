import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton
from jeu.IHM.Bouton1 import Bouton1


class PageGraphique:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1
        self.Fullscreen = False
        self.bp = Bouton1(300, 500,Etat.OPTION)
        self.bpFullNo = Bouton(520, 210, False)
        self.bpFullYes = Bouton(520, 210, False)

    def update(self):

        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Graphique :', (300, 10))

        core.Draw.text(self.couleur, 'Fullscreen :', (300, 200))

        self.bpFullNo.show()
        self.bpFullYes.show()

        if self.Fullscreen:
            core.Draw.text(self.couleur, 'No', (500, 200))
        else:
            core.Draw.text(self.couleur, 'Yes', (500, 200))

        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Retour ', (340, 480))



        if (self.startMenu == 0) or (not core.getMouseLeftClick()):
            self.startMenu = 0

            if core.getMouseLeftClick() and self.distanceCheck(self.bpFullNo) and self.Fullscreen:
                self.startMenu = 1
                self.Fullscreen = False

            if core.getMouseLeftClick() and self.distanceCheck(self.bpFullYes) and not self.Fullscreen:
                self.startMenu = 1
                self.Fullscreen = True

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False
