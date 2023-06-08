class Sauvegarde():
    def __init__(self, nom, score):
        self.nom = nom
        self.score = float(score)

    def getSauvegarde(self):
        return (self.nom) + ',' + str(self.score)
