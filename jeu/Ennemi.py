import random

from pygame import Vector2

import core
from jeu.Etat import Etat


class Ennemi:
    def __init__(self):  # constructeur
        self.vitesse = 5
        self.vitesseY = 50
        self.position = (random.randint(0, 700), 100)
        self.mass = 20

        #0 = Droite 1 = Gauche
        self.sens = 0

        core.memory("textureEnemy", core.Texture("./Image/Enemy.png", self.position, 0, (50, 50)))

    def show(self):
        if not core.memory("textureEnemy").ready:
            core.memory("textureEnemy").load()
        core.memory("textureEnemy").pos = self.position
        core.memory("textureEnemy").show()

    def deplacementEnnemi(self):
        if self.sens == 0:
            self.position = (self.position[0] + self.vitesse, self.position[1])

        if self.sens == 1:
            self.position = (self.position[0] - self.vitesse, self.position[1])

    def collisionMissile(self, missile):
        pos1 = Vector2(self.position) +(25,25)
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
        elif self.position[0] < 0:
            self.sens = 0
            self.position = (self.position[0], self.position[1] + self.vitesseY)

    def collisionJoueur(self,Joueur):
        pos1 = Vector2(self.position)
        pos2 = Vector2(Joueur.position)
        distance = pos1 - pos2
        if self.mass + Joueur.mass > distance.length():
            core.memory('etat', Etat.GAMEOVER)
