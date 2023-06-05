import core
from jeu.IHM.BarreAmelioration import BarreAmelioration
from jeu.IHM.Bouton1 import Bouton1


class MenuAchat:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1
        core.memory("TextureAchat", core.Texture('./Image/MenuAchat.png', (65, 50), 0, (650, 500)))
        self.position = core.memory("TextureAchat").pos
        self.money = 0

        self.barreameMuni = BarreAmelioration(130, 375)
        self.vitesseVaisseau = BarreAmelioration(130, 465)
        self.nbTir = BarreAmelioration(325, 375)
        self.vitesseMunition = BarreAmelioration(325, 465)

        self.MuniP = 1
        self.MuniB = Bouton1(255, 163, "")

        self.VVP = 1
        self.VVB = Bouton1(335, 265, "")

        self.NBTP = 1
        self.NBTB = Bouton1(600, 163, "")

        self.VMP = 1
        self.VMB = Bouton1(620, 265, "")

    def affichageMenu(self, VaisseauV):
        if not core.memory("TextureAchat").ready:
            core.memory("TextureAchat").load()
        core.memory("TextureAchat").show()

        self.barreameMuni.show()
        self.vitesseVaisseau.show()
        self.nbTir.show()
        self.vitesseMunition.show()

        self.MuniB.show()
        self.VVB.show()
        self.NBTB.show()
        self.VMB.show()

        core.Draw.text((255, 255, 255), str(core.memory("maPartie").money),
                       (520 + self.position[0] - 25 * (len(str(self.money))), 355 + self.position[1]), 50)

        core.Draw.text((255, 255, 255), "Munition :", (150, 150), 20)
        core.Draw.text((255, 255, 255), "Vitesse du Vaisseau :", (150, 250), 20)
        core.Draw.text((255, 255, 255), "Nombre de Tir :", (450, 150), 20)
        core.Draw.text((255, 255, 255), "Vitesse du Missile :", (450, 250), 20)

        core.Draw.text((0, 0, 0), str(self.MuniP), (250, 150), 20)
        core.Draw.text((0, 0, 0), str(self.VVP), (330, 253), 20)
        core.Draw.text((0, 0, 0), str(self.NBTP), (595, 150), 20)
        core.Draw.text((0, 0, 0), str(self.VMP), (615, 253), 20)

        if self.MuniB.update1():
            if self.barreameMuni.stat < 4:
                if core.memory("maPartie").money >= self.MuniP:
                    self.barreameMuni.stat += 1
                    core.memory("maPartie").money -= self.MuniP
                    self.MuniP *= 2
                    core.memory("maPartie").munition += 1

        if self.VVB.update1():
            if self.vitesseVaisseau.stat < 4:
                if core.memory("maPartie").money >= self.VVP:
                    self.vitesseVaisseau.stat += 1
                    core.memory("maPartie").money -= self.VVP
                    self.VVP *= 2
                    self.speedincreeseJoueur(VaisseauV)

        if self.NBTB.update1():
            if self.nbTir.stat < 4:
                if core.memory("maPartie").money >= self.NBTP:
                    self.nbTir.stat += 1
                    core.memory("maPartie").money -= self.NBTP
                    self.NBTP *= 2

        if self.VMB.update1():
            if self.vitesseMunition.stat < 4:
                if core.memory("maPartie").money >= self.VMP:
                    self.vitesseMunition.stat += 1
                    core.memory("maPartie").money -= self.VMP
                    self.VMP *= 2
                    core.memory("maPartie").Vmissile *= 1.4

    def speedincreeseJoueur(self, Joueur):
        Joueur.speed *= 1.3
