from pygame import Vector2

import core
from jeu.Coin import Coin
from jeu.Ennemi import Ennemi
from jeu.Etat import Etat
from jeu.IHM.MenuAchat import MenuAchat
from jeu.Missile import Missile
from jeu.Vaisseau import Vaisseau

from random import randint


class Partie:
    def __init__(self):  # constructeur

        self.couleur = (255, 255, 255)
        self.taille = Vector2(800, 600)
        self.munition = 3
        self.monVaisseau = Vaisseau
        self.monMissile = []
        self.nbEnnemis = 3
        self.ennemis = []
        self.AntiRebond = 1
        self.MissileAntiRebond = 1
        self.Coins = []
        self.money = 0
        self.MenuAchat = MenuAchat()
        self.ActiveMenuAchat = False

        self.score = 0

        core.memory("son", core.Sound("./Sound/piouu1.mp3"))

    def addJoueur(self):
        self.monVaisseau = Vaisseau()

    def addMissile(self):
        for i in range(self.munition):
            self.monMissile.append(Missile(1200))

    def show(self):
        self.monVaisseau.show()

    def update(self):

        if (self.AntiRebond == 0) or (not core.getKeyPressList('e')):
            self.AntiRebond = 0
            if core.getKeyPressList('e'):
                self.AntiRebond = 1

                if self.ActiveMenuAchat:
                    self.ActiveMenuAchat = False
                else:
                    self.ActiveMenuAchat = True

        if not self.ActiveMenuAchat:
            self.updateJeu()
        else:
            self.updateAchat()

    def updateAchat(self):
        self.MenuAchat.affichageMenu()

    def updateJeu(self):
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
        self.updateCoins()

        if core.getKeyPressList('ESCAPE'):
            core.memory('etat', Etat.PAUSE)

    def updateEnnemis(self):
        for e in self.ennemis:
            e.edge()
            e.deplacementEnnemi()
            e.show()

            for i in self.monMissile:
                if e.collisionMissile(i):
                    i.alive = False
                    self.addCoin(e.position[0],e.position[1])
                    i.position = (1200, 1200)
                    e.position = (randint(0, 700), 100)
                    e.sens = 0
                    self.score = self.score + 1
                    print(str(self.score))
                    if self.score > 10:
                        self.nbEnnemis = self.score / 5 + 3
            e.collisionJoueur(self.monVaisseau)

    def tirer(self):

        for i in self.monMissile:
            if not i.isAlive():
                i.alive = True
                core.memory("son").pause()
                core.memory("son").rewind()
                core.memory("son").start()
                i.deplacementMissile(self.monVaisseau.getPosX())
                break

    def addEnnemis(self):
        if len(self.ennemis) < self.nbEnnemis:
            self.ennemis.append(Ennemi())

    def restart(self):
        core.memory("maPartie").addEnnemis()
        self.score = 0
        self.nbEnnemis = 3
        for i in range(len(self.monMissile)):
            self.monMissile.pop()
        for i in range(len(self.ennemis)):
            self.ennemis.pop()
        core.memory("maPartie").addMissile()

    def get_score(self):
        return self.score

    def addCoin(self, CoordX, CoordY):
        Chance = randint(1, 5)
        if Chance == 1:
            self.Coins.append(Coin(CoordX, CoordY))

    def updateCoins(self):
        for i in self.Coins:
            if i.collisionJoueur(self.monVaisseau):
                self.money += i.gain
                index = self.Coins.index(i)
                self.Coins.pop(index)
            elif i.update() == 1:
                index = self.Coins.index(i)
                self.Coins.pop(index)


