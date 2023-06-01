from pygame import Vector2

import core
from jeu.Ennemi import Ennemi
from jeu.Etat import Etat
from jeu.Missile import Missile
from jeu.Vaisseau import Vaisseau


class Partie:
    def __init__(self):  # constructeur

        self.couleur = (255, 255, 255)
        self.taille = Vector2(800, 600)
        self.munition = 3
        self.monVaisseau = Vaisseau
        self.monMissile = []
        self.nbEnnemis = 3
        self.ennemis = []
        self.MissileAntiRebond = 1

        self.score = 0
        # core.memory("son", core.Sound("./Sound/piouu1.mp3"))

    def addJoueur(self):
        self.monVaisseau = Vaisseau()

    def addMissile(self):
        for i in range(self.munition):
            self.monMissile.append(Missile(1200))


    def show(self):
        self.monVaisseau.show()

    def update(self):
        core.Draw.text(self.couleur, 'Score: ' + str(self.score), (10, 10))
        self.monVaisseau.deplacement()

        if (self.MissileAntiRebond == 0) or (not core.getKeyPressList('SPACE')):
            self.MissileAntiRebond = 0
            if core.getKeyPressList('SPACE'):
                self.MissileAntiRebond = 1
                self.tirer()



        self.monVaisseau.show()

        for i in self.monMissile:
            i.show()
            i.trajectoire()
            i.collision()

        self.updateEnnemis()

        if core.getKeyPressList('ESCAPE'):
            core.memory('etat', Etat.PAUSE)

    def updateEnnemis(self):
        for e in self.ennemis:
            e.edge()
            e.deplacementEnnemi()
            e.show()

            for i in self.monMissile:
                if e.collisionMissile(i):
                    self.score = self.score + 1
                    print(str(self.score))
                    if self.score > 10:
                        self.nbEnnemis = self.score / 5 + 3
            e.collisionJoueur(self.monVaisseau)

    def tirer(self):

        for i in self.monMissile:
            if not i.isAlive():
                i.alive = True
                # core.memory("son").pause()
                # core.memory("son").rewind()
                # core.memory("son").start()
                i.deplacementMissile(self.monVaisseau.getPosX())
                break


    def addEnnemis(self):
        if len(self.ennemis) < self.nbEnnemis:
            self.ennemis.append(Ennemi())

    def restart(self):
        core.memory("maPartie").addEnnemis()
        core.memory('etat', Etat.MENU)
        self.score = 0
        self.nbEnnemis = 3
        for i in range(len(self.monMissile)):
            self.monMissile.pop()
        for i in range (len(self.ennemis)):
            self.ennemis.pop()
        core.memory("maPartie").addMissile()

    def get_score(self):
        return self.score
