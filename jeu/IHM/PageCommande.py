import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageCommande:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.bp3 = Bouton(300, 500)
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2
        self.startMenu = 1

    def update(self):
        self.mouse = core.getMouseLocation()
        core.Draw.text(self.couleur, 'Commande:', (300, 10))
        core.Draw.text(self.couleur, 'Gauche: q ', (340, 180))
        core.Draw.text(self.couleur, 'Droite: d ', (340, 280))
        core.Draw.text(self.couleur, 'Tirer: espace', (340, 380))
        self.bp3.show()
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
