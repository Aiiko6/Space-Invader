import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageSkin:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)

        self.bp3 = Bouton(300, 500)
        self.Flechedroite = Bouton(150, 200, True,"./Image/Fleche_droite.png")
        self.FlecheGauche = Bouton(600, 200, True, "./Image/Fleche_gauche.png")
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2
        self.startMenu = 1

    def update(self):

        self.mouse = pygame.mouse.get_pos()

        self.bp3.show()
        self.Flechedroite.show()
        self.FlecheGauche.show()
        core.Draw.text(self.couleur, 'Retour ', (340, 480))

        if (self.startMenu == 0) or (not core.getMouseLeftClick()):
            self.startMenu = 0

            if core.getMouseLeftClick() and self.distanceCheck(self.bp3):
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
