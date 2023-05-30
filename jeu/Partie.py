from pygame import Vector2

import core
from jeu.Ennemi import Ennemi
from jeu.Missile import Missile
from jeu.Vaisseau import Vaisseau



class Partie:
    def __init__(self):  # constructeur

        self.couleur = (255, 255, 255)
        self.taille = Vector2(800, 600)

        self.monVaisseau = Vaisseau
        self.monMissile = Missile

        self.nbEnnemis = 3
        self.ennemis = []

        self.score = 0

    def addJoueur(self):
            self.monVaisseau = Vaisseau()

    def addMissile(self):
        self.monMissile = Missile(1200)

    def show(self):
        self.monVaisseau.show()

    def update(self):
        core.Draw.text(self.couleur, 'score: ' + str(self.score),(10,10))
        self.monVaisseau.deplacement()
        if core.getKeyPressList("g"):
            self.tirer()
        self.monVaisseau.show()
        self.monMissile.show()

        self.monMissile.trajectoire()
        self.monMissile.collision()
        self.updateEnnemis()

    def updateEnnemis(self):
        for e in self.ennemis:
            e.edge()
            e.deplacementEnnemi()
            e.show()
            if e.collisionMissile(self.monMissile):
                self.score = self.score + 1
                print(str(self.score))
                if (self.score > 10):
                    self.nbEnnemis = self.score/10 + 3




    def tirer(self):
        self.monMissile.deplacementMissile(self.monVaisseau.getPosX())

    def addEnnemis(self):
        if len(self.ennemis) < self.nbEnnemis:
            self.ennemis.append(Ennemi())
