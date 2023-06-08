from jeu import core
from jeu.Leaderboard.Sauvegarde import Sauvegarde


class Classement():
    def __init__(self):
        self.classement = []

    def getFile(self):
        self.classement.clear()

        nb_ligne = core.memory("gestionFichier").compterLigne()
        print(nb_ligne)
        for i in range (nb_ligne):
            ligne = core.memory("gestionFichier").lireLigne(i)  #Recupere la ligne indice i
            #print(ligne)
            lignesplit = ligne.split(', ')  #Sépare le nom du score
            #print(lignesplit[0])
            #print(lignesplit[1])
            self.classement.append(Sauvegarde(lignesplit[0],lignesplit[1]))
        self.trierTableau()


    def trierTableau(self):
        self.classement.sort(key=lambda Sauvegarde: Sauvegarde.score, reverse=True)

        for e in self.classement:
            txt = e.getSauvegarde()

    def getScore(self,num):
        self.trierTableau()
        var = self.classement[num]
        txt = var.getSauvegarde()
        return txt


