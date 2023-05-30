import sys

import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageGameOver:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton(300,200)
        self.bp1 = Bouton(300, 300)
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2


    def update(self):
        core.Draw.text(self.couleur, 'Game OVER ', (320, 10))
        self.mouse = pygame.mouse.get_pos()


        self.bp.show()
        if core.getMouseLeftClick() and self.distanceCheck(self.bp):
            core.memory("maPartie").restart()
            core.memory("maPartie").addEnnemis()
            core.memory('etat', Etat.JEU)
        core.Draw.text(self.couleur, 'Rejouer ', (340, 180))

        self.bp1.show()
        if core.getMouseLeftClick() and self.distanceCheck(self.bp1):
            pygame.quit()
            sys.exit()
        core.Draw.text(self.couleur, 'Exit ', (340, 280))

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False