import sys

import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton
from jeu.IHM.Bouton1 import Bouton1


class PageGameOver:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton1(300,200,Etat.MENU)
        self.bp1 = Bouton1(300, 400,Etat.DESTROY)
        self.massCursor = 2
        self.bRunOnce = 0
        self.score = 0


    def update(self):
        core.memory("maPartie").restart()
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Rejouer ', (340, 180))

        self.bp1.show()
        self.bp1.update()

        core.Draw.text(self.couleur, 'Score: ' + str(self.score), (340, 280))
        core.Draw.text(self.couleur, 'Exit ', (340, 380))

    def setScore(self):
        self.score = core.memory("maPartie").get_score()

