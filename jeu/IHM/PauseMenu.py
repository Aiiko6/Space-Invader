import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PauseMenu:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton(300,200)
        self.bp1 = Bouton(300, 300)
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2


    def update(self):
        self.mouse = pygame.mouse.get_pos()

        core.Draw.text(self.couleur, 'Pause :', (300, 10))

        self.bp.show()
        if core.getMouseLeftClick() and self.distanceCheck(self.bp):
            core.memory('etat', Etat.JEU)
        core.Draw.text(self.couleur, 'Reprendre ', (340, 180))

        self.bp1.show()
        if core.getMouseLeftClick() and self.distanceCheck(self.bp1):
            core.memory('etat', Etat.MENU)
        core.Draw.text(self.couleur, 'Exit ', (340, 280))

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False