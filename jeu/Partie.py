from pygame import Vector2

import core
from jeu.Coin import Coin
from jeu.Ennemi import Ennemi
from jeu.Etat import Etat
from jeu.Fire import Fire
from jeu.IHM.MenuAchat import MenuAchat
from jeu.Missile import Missile
from jeu.Vaisseau import Vaisseau

from random import randint


class Partie:
    def __init__(self):  # constructeur

        self.couleur = (255, 255, 255)
        self.taille = Vector2(800, 600)
        self.munitionMax = 3
        self.NbTir = 1
        self.munition = self.munitionMax * self.NbTir
        self.monVaisseau = Vaisseau
        self.monMissile = []
        self.nbEnnemis = 3
        self.ennemis = []
        self.AntiRebond = 1
        self.MissileAntiRebond = 1
        self.Coins = []
        self.Fires = []
        self.money = 30
        self.MenuAchat = MenuAchat()
        self.ActiveMenuAchat = False
        self.vieMob = 1
        self.degatMissile = 1

        self.Vmissile = 10

        self.score = 190

        core.memory("son", core.Sound("./Sound/piouu1.mp3", 1))

    def addJoueur(self):
        self.monVaisseau = Vaisseau()

    def addMissile(self):
        for i in range(self.munition - len(self.monMissile)):
            self.monMissile.append(Missile(1200, self.Vmissile))

    def show(self):
        self.monVaisseau.show()

    def update(self):
        self.munition = self.munitionMax * self.NbTir
        self.addMissile()
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
        self.MenuAchat.affichageMenu(self.monVaisseau)

    def updateJeu(self):
        core.Draw.text(self.couleur, 'Score: ' + str(self.score), (10, 10))
        self.monVaisseau.deplacement()

        self.addEnnemis()

        if (self.MissileAntiRebond == 0) or (not core.getKeyPressList('SPACE')):
            self.MissileAntiRebond = 0
            if core.getKeyPressList('SPACE'):
                self.MissileAntiRebond = 1
                self.tirer()

        self.monVaisseau.show()

        for i in self.monMissile:
            i.show()
            i.trajectoire()
            if i.collision():
                index = self.monMissile.index(i)
                self.monMissile.pop(index)

        self.updateEnnemis()
        self.updateCoins()
        self.updateFire()

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
                    self.addCoin(e.position[0], e.position[1])
                    self.addFire(e.position[0], e.position[1])
                    if e in self.ennemis:
                        if e.vie <= self.degatMissile:
                            index = self.ennemis.index(e)
                            self.ennemis.pop(index)
                            self.score = self.score + 1
                        else:
                            e.vie -= self.degatMissile

                        i.position = (1200, 1200)

                    print(str(self.score))
                    if self.score <= 50:

                        self.nbEnnemis = self.score / 20 + 3

                    elif self.score > 50 and self.score <= 100:
                        self.vieMob = 2
                        self.nbEnnemis = self.score / 50 + 3

                    elif self.score > 100 and self.score <= 200:
                        self.vieMob = 3
                        self.nbEnnemis = self.score / 90 + 3

                    elif self.score > 300:
                        self.vieMob = 4
                        self.nbEnnemis = self.score / 90 + 3

            e.collisionJoueur(self.monVaisseau)

    def tirer(self):
        MissileAvaible = []
        Compteur = 0

        for i in self.monMissile:
            if not i.isAlive():
                Compteur += 1
                i.alive = True
                MissileAvaible.append(i)
            if Compteur >= self.NbTir:
                break

        if Compteur > 0:
            core.memory("son").pause()
            core.memory("son").rewind()
            core.memory("son").start()
            if Compteur == 1:
                MissileAvaible[0].deplacementMissile(self.monVaisseau.getPosX())
            elif Compteur == 2:
                MissileAvaible[0].deplacementMissile(self.monVaisseau.getPosX() - 10)
                MissileAvaible[1].deplacementMissile(self.monVaisseau.getPosX() + 10)
            elif Compteur == 3:
                MissileAvaible[0].deplacementMissile(self.monVaisseau.getPosX()-20)
                MissileAvaible[1].deplacementMissile(self.monVaisseau.getPosX())
                MissileAvaible[2].deplacementMissile(self.monVaisseau.getPosX()+20)
            elif Compteur == 4:
                MissileAvaible[0].deplacementMissile(self.monVaisseau.getPosX() + 40)
                MissileAvaible[1].deplacementMissile(self.monVaisseau.getPosX() + 20)
                MissileAvaible[2].deplacementMissile(self.monVaisseau.getPosX() - 20)
                MissileAvaible[3].deplacementMissile(self.monVaisseau.getPosX() - 40)


    def addEnnemis(self):
        if len(self.ennemis) < self.nbEnnemis:
            print(self.vieMob)
            self.ennemis.append(Ennemi(self.vieMob))

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

    def addFire(self, CoordX, CoordY):
        self.Fires.append(Fire(CoordX, CoordY))

    def updateFire(self):
        for i in self.Fires:
            i.update()
            if i.getTimeToLive() == 15:
                index = self.Fires.index(i)
                self.Fires.pop(index)
