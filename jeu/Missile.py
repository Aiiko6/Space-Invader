import core


class Missile:
    def __init__(self,coordX): #constructeur
        self.vitesse = 10
        self.couleur = (255, 0, 0)
        self.position =(coordX,550)
        self.mass = 5

        self.lance = False



    def show(self):
        core.Draw.circle(self.couleur,self.position,self.mass)

    def deplacementMissile(self,X):
        self.position = ( X , 550)

    def trajectoire(self):
        if (self.position[0] > 0) and (self.position[0] < 800):
            self.position = (self.position[0],self.position[1] + (self.vitesse * -1 ))

    def collision(self):
        #Si dépassement de l'écran
        if (self.position[1] > 600):
            self.position = (1200,1200)
