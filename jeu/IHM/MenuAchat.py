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
        self.barreDegat = BarreAmelioration(130, 465)
        self.nbTir = BarreAmelioration(325, 375)
        self.vitesseMunition = BarreAmelioration(325, 465)

        self.MuniP = 1
        self.MuniB = Bouton1(255, 163, "")

        self.DegatP = 1
        self.DegatB = Bouton1(335, 265, "")

        self.NBTP = 1
        self.NBTB = Bouton1(600, 163, "")

        self.VMP = 1
        self.VMB = Bouton1(620, 265, "")

    def affichageMenu(self, VaisseauV):
        if not core.memory("TextureAchat").ready:
            core.memory("TextureAchat").load()
        core.memory("TextureAchat").show()

        self.barreameMuni.show()
        self.barreDegat.show()
        self.nbTir.show()
        self.vitesseMunition.show()

        self.MuniB.show()
        self.DegatB.show()
        self.NBTB.show()
        self.VMB.show()

        core.Draw.text((255, 255, 255), str(core.memory("maPartie").money),
                       (520 + self.position[0] - 25 * (len(str(self.money))), 355 + self.position[1]), 50)

        core.Draw.text((255, 255, 255), "Munition :", (150, 150), 20)
        core.Draw.text((255, 255, 255), "Point de Dégât :", (150, 250), 20)
        core.Draw.text((255, 255, 255), "Nombre de Tir :", (450, 150), 20)
        core.Draw.text((255, 255, 255), "Vitesse du Missile :", (450, 250), 20)

        core.Draw.text((0, 0, 0), str(self.MuniP), (250, 150), 20)
        core.Draw.text((0, 0, 0), str(self.DegatP), (330, 253), 20)
        core.Draw.text((0, 0, 0), str(self.NBTP), (595, 150), 20)
        core.Draw.text((0, 0, 0), str(self.VMP), (615, 253), 20)

        if self.MuniB.update1():
            if self.barreameMuni.stat < 4:
                if core.memory("maPartie").money >= self.MuniP:
                    self.barreameMuni.stat += 1
                    core.memory("maPartie").money -= self.MuniP
                    self.MuniP *= 2
                    core.memory("maPartie").munitionMax += 1

        if self.DegatB.update1():
            if self.barreDegat.stat < 4:
                if core.memory("maPartie").money >= self.DegatP:
                    self.barreDegat.stat += 1
                    core.memory("maPartie").money -= self.DegatP
                    self.DegatP *= 2
                    core.memory("maPartie").degatMissile += 1

        if self.NBTB.update1():
            if self.nbTir.stat < 4:
                if core.memory("maPartie").money >= self.NBTP:
                    self.nbTir.stat += 1
                    core.memory("maPartie").money -= self.NBTP
                    self.NBTP *= 2
                    core.memory("maPartie").NbTir += 1

        if self.VMB.update1():
            if self.vitesseMunition.stat < 4:
                if core.memory("maPartie").money >= self.VMP:
                    self.vitesseMunition.stat += 1
                    core.memory("maPartie").money -= self.VMP
                    self.VMP *= 2
                    core.memory("maPartie").Vmissile *= 1.1

    def speedincreeseJoueur(self, Joueur):
        Joueur.speed *= 1.3
