import sys

import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton
from jeu.IHM.Bouton1 import Bouton1


class PageMenu:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)

        self.bp = Bouton1(300, 200, Etat.CHARGEMENT)
        self.bp1 = Bouton1(300, 300, Etat.OPTION)
        self.bp2 = Bouton1(300, 400,Etat.COM)
        self.bp3 = Bouton1(300, 500,Etat.DESTROY)


    def update(self):
        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Space invader: ', (300, 10))
        self.bp.show()
        self.bp.update()


        core.Draw.text(self.couleur, 'Jouer ', (340, 180))

        self.bp1.show()
        self.bp1.update()
        core.Draw.text(self.couleur, 'Parametres ', (340, 280))
        self.bp2.show()
        self.bp2.update()
        core.Draw.text(self.couleur, 'Commandes ', (340, 380))
        self.bp3.show()
        self.bp3.update()
        core.Draw.text(self.couleur, 'Quitter ', (340, 480))

