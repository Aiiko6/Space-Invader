import random

from pygame import Vector2

import core
from jeu.Etat import Etat


class Boss:
    def __init__(self):  # constructeur
        self.vie = 200
        self.vitesse = 1.1
        self.vitesseY = 50
        self.position = (-5000, -5000)
        self.mass = 400
        self.alive = False
        core.memory("textureBoss", core.Texture("./Image/Boss.png", (0, 0), 0, (800,600)))

    def show(self):
        if not core.memory("textureBoss").ready:
            core.memory("textureBoss").load()
        core.memory("textureBoss").pos = self.position
        core.memory("textureBoss").show()

    def deplacementBoss(self):
        self.position = (self.position[0], self.position[1] + self.vitesse)

    def collisionMissileBoss(self, missile):
        pos1 = Vector2(self.position) + (400, 0)
        pos2 = Vector2(missile.position)
        distance = pos1 - pos2
        if self.mass + missile.mass > distance.length():
            return True

    def collisionJoueur(self, Joueur):
        pos1 = Vector2(self.position) + (400, 0)
        pos2 = Vector2(Joueur.position)
        distance = pos1 - pos2
        if self.mass + Joueur.mass > distance.length():
            core.memory('etat', Etat.GAMEOVER)
            core.memory('PageGameOver').setScore()

    def isAlive(self):
        return self.alive
