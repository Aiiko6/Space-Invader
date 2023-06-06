class Sauvegarde():
    def __init__(self, nom, score):
        self.nom = nom
        self.score = int(score)

    def getSauvegarde(self):
        print(self.nom + ',' + str(self.score))
