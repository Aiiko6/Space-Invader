from jeu import core
from jeu.Leaderboard.Sauvegarde import Sauvegarde


class Classement():
    def __init__(self):
        self.classement = []

    def getFile(self):
        for i in self.classement:  #Vider le tableau pour MAJ
            self.classement.pop()

        nb_ligne = core.memory("gestionFichier").compterLigne()
        for i in range (nb_ligne):
            ligne = core.memory("gestionFichier").lireLigne(i)  #Recupere la ligne indice i
            #print(ligne)
            lignesplit = ligne.split(', ')  #Sépare le nom du score
            #print(lignesplit[0])
            #print(lignesplit[1])
            self.classement.append(Sauvegarde(lignesplit[0],lignesplit[1]))
        self.trierTableau()


    def addScore(self):
        pass

    def trierTableau(self):
        self.classement.sort(key=lambda Sauvegarde: Sauvegarde.score, reverse=True)

        for e in self.classement:
            e.getSauvegarde()


