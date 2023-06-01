import pygame
from pygame import Vector2

import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class MenuAchat:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1

    def affichageMenu(self):
        if not core.memory("TextureAchat").ready:
            core.memory("TextureAchat").load()
        core.memory("TextureAchat").pos = (self.position[0] - 25, self.position[1] - 25)
        core.memory("TextureAchat").show()