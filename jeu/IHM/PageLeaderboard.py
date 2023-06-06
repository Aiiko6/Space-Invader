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

        self.top1 = self.classsement = core.memory("Classement").getScore(0)
        self.top2 = self.classsement = core.memory("Classement").getScore(1)
        self.top3 = self.classsement = core.memory("Classement").getScore(2)
        self.top4 = self.classsement = core.memory("Classement").getScore(3)
        self.top5 = self.classsement = core.memory("Classement").getScore(4)


        core.Draw.text(self.couleur, 'LEADERBOARD:', (300, 10))
        core.Draw.text(self.couleur, self.top1, (300, 100))
        core.Draw.text(self.couleur, self.top2, (300, 150))
        core.Draw.text(self.couleur, self.top3, (300, 200))
        core.Draw.text(self.couleur, self.top4, (300, 250))
        core.Draw.text(self.couleur, self.top5, (300, 300))
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Retour ', (340, 480))
