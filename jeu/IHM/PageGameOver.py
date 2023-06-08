from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageGameOver:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.bp = Bouton1(300,200,Etat.MENU)
        self.bp1 = Bouton1(300, 500,Etat.SAUVEGARDE)
        self.massCursor = 2
        self.bRunOnce = 0
        self.score = 0
        self.money = 0
        self.nombreCoup = 0
        self.scoreMulti =0


    def update(self):
        core.memory("maPartie").restart()
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Rejouer ', (340, 180))

        self.bp1.show()
        self.bp1.update()

        core.Draw.text(self.couleur, 'Kill: ' + str(self.score), (275, 230))
        core.Draw.text(self.couleur, 'Nombre coup: ' + str(self.nombreCoup), (275, 280))
        core.Draw.text(self.couleur, 'Nombre coins: ' + str(self.money), (275, 330))
        core.Draw.text(self.couleur, 'Score: kill + coin - (Nombre coup /2): ' + str(self.scoreMulti), (275, 380))
        core.Draw.text(self.couleur, 'Sauvegarder ', (340, 480))

    def setScore(self):
        self.score = core.memory("maPartie").get_score()
        self.nombreCoup = core.memory("maPartie").get_nombreCoup()
        self.money = core.memory("maPartie").get_money()

        self.scoreMulti = self.score + self.money - (self.nombreCoup /2)


