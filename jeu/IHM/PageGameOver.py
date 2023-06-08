from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageGameOver:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.posbp3 = (400 - (190 / 2), 525 - 25)
        self.bp3 = Bouton1(self.posbp3[0], self.posbp3[1], Etat.MENU, True, "./Image/Template.png", (190, 50))
        self.massCursor = 2
        self.bRunOnce = 0
        self.score = 0
        self.money = 0
        self.nombreCoup = 0
        self.scoreMulti =0

        self.posbp4 = (30, 570)
        self.bp4 = Bouton1(self.posbp4[0], self.posbp4[1], Etat.SAUVEGARDE, True, "./Image/Template.png", (275, 50))


    def update(self):
        core.memory("maPartie").restart()

        if not core.memory("TexTitre").ready:
            core.memory("TexTitre").load()
        core.memory("TexTitre").show()

        core.Draw.text((0,0,0), 'GAME OVER ', (200, 80), 40, "./Font/8-BIT WONDER.TTF", False)

        self.bp3.show()
        self.bp3.updateRect()
        core.Draw.text((0,0,0), 'Retour ', (self.posbp3[0] + 5, self.posbp3[1] - 13), 20,
                       "./Font/8-BIT WONDER.TTF", False)

        core.Draw.text(self.couleur, 'Kill ' + str(self.score), (275, 230))
        core.Draw.text(self.couleur, 'Nombre coup ' + str(self.nombreCoup), (275, 280))
        core.Draw.text(self.couleur, 'Nombre coins ' + str(self.money), (275, 330))
        core.Draw.text(self.couleur, 'Score: kill + coin - (Nombre coup /2) :' + str(self.scoreMulti), (275, 380))

        self.bp4.show()
        self.bp4.updateRect()
        core.Draw.text((0,0,0), 'Sauvegarder ', (self.posbp4[0] + 5, self.posbp4[1] - 13), 20,
                       "./Font/8-BIT WONDER.TTF", False)

    def setScore(self):
        self.score = core.memory("maPartie").get_score()
        self.nombreCoup = core.memory("maPartie").get_nombreCoup()
        self.money = core.memory("maPartie").get_money()

        self.scoreMulti = self.score + self.money - (self.nombreCoup /2)


