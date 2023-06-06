import pygame

from jeu import core
from jeu.Etat import Etat


class PageChargement:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.timer = 0
        self.vitesse = 10

    def update(self):

        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Chargement :', (300, 10))

        core.Draw.rect((255, 255, 255), (100, 400, 600, 100))

        self.timer = self.timer + self.vitesse

        if self.timer == 500:
            self.vitesse = 1

        if self.timer == 560:
            self.timer = 0
            self.vitesse = 10
            core.memory("etat", Etat.JEU)

        core.Draw.rect((15, 167, 15), (120, 420, self.timer, 60))




