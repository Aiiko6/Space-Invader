import pygame
from pygame import Vector2

from jeu import core


class Bouton1:
    def __init__(self, coordX, coordY, var, Visible=True, URL=""):  # constructeur
        self.Adresse = URL
        self.visible = Visible
        self.couleur = (255, 255, 255)
        self.mass = 20
        self.position = (coordX, coordY)
        self.positionImage = (coordX - 50 / 2, coordY - 50 / 2)
        self.Skin = core.Texture(URL, self.positionImage, 0, (50, 50))
        self.var = var
        self.massCursor = 2
        self.mouse = ""

    def show(self):
        if self.visible:
            if self.Adresse == "":
                core.Draw.circle(self.couleur, self.position, self.mass)
            else:
                if not self.Skin.ready:
                    self.Skin.load()
                self.Skin.show()

    def update(self):
        if self.distanceCheck() and core.memory('gestionFront').update():
            print(self.var)
            print(self.var.value)
            core.memory('etat', self.var)

    def update1(self):
        if self.distanceCheck() and core.memory('gestionFront').update():
            return True

    def distanceCheck(self):
        self.mouse = pygame.mouse.get_pos()
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(self.position)
        distance = pos1 - pos2
        if self.massCursor + self.mass > distance.length():
            return True
        else:
            return False
