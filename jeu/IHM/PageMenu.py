import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageMenu:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton(300,200)
        self.bp1 = Bouton(300, 300)
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2


    def update(self):
        self.mouse = pygame.mouse.get_pos()

        core.Draw.text(self.couleur, 'Space invader: ', (300, 10))
        self.bp.show()
        if core.getMouseLeftClick() and self.distanceCheck(self.bp):
            core.memory('etat', Etat.JEU)

        core.Draw.text(self.couleur, 'Jouer ', (340, 180))
        self.bp1.show()
        core.Draw.text(self.couleur, 'Parametres ', (340, 280))

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False