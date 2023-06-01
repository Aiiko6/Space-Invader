import sys

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
        self.bp2 = Bouton(300, 400)
        self.bp3 = Bouton(300, 500)
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2
        self.startMenu = 1


    def update(self):
        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Space invader: ', (300, 10))
        self.bp.show()
        core.Draw.text(self.couleur, 'Jouer ', (340, 180))
        self.bp1.show()
        core.Draw.text(self.couleur, 'Parametres ', (340, 280))
        self.bp2.show()
        core.Draw.text(self.couleur, 'Commandes ', (340, 380))
        self.bp3.show()
        core.Draw.text(self.couleur, 'Quitter ', (340, 480))

        if (self.startMenu == 0) or (not core.getMouseLeftClick()):
            self.startMenu = 0
            if core.getMouseLeftClick() and self.distanceCheck(self.bp):
                self.startMenu = 1
                core.memory('etat', Etat.JEU)
            if core.getMouseLeftClick() and self.distanceCheck(self.bp1):
                self.startMenu = 1
                core.memory('etat', Etat.OPTION)
            if core.getMouseLeftClick() and self.distanceCheck(self.bp2):
                self.startMenu = 1
                core.memory('etat', Etat.COM)
            if core.getMouseLeftClick() and self.distanceCheck(self.bp3):
                self.startMenu = 1
                pygame.quit()
                sys.exit()

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False