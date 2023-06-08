import pygame
from pygame import Vector2

from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton
from jeu.IHM.Bouton1 import Bouton1


class PauseMenu:
    def __init__(self):  # constructeur
        self.couleur = (0, 0, 0)

        self.posbp = (430 - (230 / 2), 300 - 25)
        self.posbp1 = (430 - (140 / 2), 375 - 25)

        self.bp = Bouton1(self.posbp[0], self.posbp[1], Etat.JEU, True, "./Image/Template.png", (230, 50))
        self.bp1 = Bouton1(self.posbp1[0], self.posbp1[1], Etat.MENU, True, "./Image/Template.png", (140, 50))
        print(self.bp.scale)

        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1

    def update(self):
        self.mouse = pygame.mouse.get_pos()

        if not core.memory("TexTitre").ready:
            core.memory("TexTitre").load()
        core.memory("TexTitre").show()

        core.Draw.text(self.couleur, 'Pause ', (300, 80), 40, "./Font/8-BIT WONDER.TTF", False)
        self.bp.show()
        self.bp.updateRect()
        core.Draw.text(self.couleur, 'Reprendre ', (self.posbp[0], self.posbp[1]-13), 20, "./Font/8-BIT WONDER.TTF", False)
        self.bp1.show()
        self.bp1.updateRect()
        core.Draw.text(self.couleur, 'Exit ', (self.posbp1[0]+7, self.posbp1[1]-13), 20, "./Font/8-BIT WONDER.TTF", False)

