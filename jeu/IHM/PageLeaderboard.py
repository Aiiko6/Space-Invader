from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageLeaderBoard:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)

        self.bp = Bouton1(300, 500, Etat.MENU)
        self.top1 = ""
        self.top2 = ""
        self.top3 = ""
        self.top4 = ""
        self.top5 = ""
        self.timer = 0

    def update(self):
        self.timer = self.timer +1
        if self.timer == 60:
            self.timer = 0
            core.memory("Classement", ).getFile()

        self.top1 = core.memory("Classement").getScore(0).replace(",",": ")
        self.top2 = core.memory("Classement").getScore(1).replace(",",": ")
        self.top3 = core.memory("Classement").getScore(2).replace(",",": ")
        self.top4 = core.memory("Classement").getScore(3).replace(",",": ")
        self.top5 = core.memory("Classement").getScore(4).replace(",",": ")


        core.Draw.text(self.couleur, 'LEADERBOARD', (200, 10),40,"./Font/8-BIT WONDER.TTF",False)
        core.Draw.text(self.couleur, self.top1, (350, 100))
        core.Draw.text(self.couleur, self.top2, (350, 150))
        core.Draw.text(self.couleur, self.top3, (350, 200))
        core.Draw.text(self.couleur, self.top4, (350, 250))
        core.Draw.text(self.couleur, self.top5, (350, 300))
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Retour ', (340, 480),20,"./Font/8-BIT WONDER.TTF",False)
