import random

from pygame import Vector2

import core


class Ennemi:
    def __init__(self):  # constructeur
        self.vitesse = 5
        self.vitesseY = 50
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.position = (random.randint(0, 700), 100)
        self.mass = 20

        #0 = Droite 1 = Gauche
        self.sens = 0

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.mass)

    def deplacementEnnemi(self):
        if self.sens == 0:
            self.position = (self.position[0] + self.vitesse, self.position[1])

        if self.sens == 1:
            self.position = (self.position[0] - self.vitesse, self.position[1])

    def collisionMissile(self, missile):
        pos1 = Vector2(self.position)
        pos2 = Vector2(missile.position)
        distance = pos1 - pos2
        if self.mass + missile.mass > distance.length():
            print('hit')
            self.position = (random.randint(0, 700), 100)

            return True

    def edge(self):
        if self.position[0] > 750:
            self.position = (self.position[0], self.position[1] + self.vitesseY)
            self.sens = 1
        elif self.position[0] < 50:
            self.sens = 0
            self.position = (self.position[0], self.position[1] + self.vitesseY)
