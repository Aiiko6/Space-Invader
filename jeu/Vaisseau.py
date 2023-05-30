import core
from PIL import Image, ImageDraw


class Vaisseau:
    def __init__(self): #constructeur
        self.vitesse = 10
        self.couleur = (255, 255, 255)
        self.position =(100,550)
        self.mass = 20



    def show(self):
        core.Draw.circle(self.couleur,self.position,self.mass)

    def deplacement(self):  #Deplacmement du vaisseau suivant les touches pressé
        if core.getKeyPressList("d") and self.position[0] < 800:
            self.position = (self.position[0] + self.vitesse, self.position[1])
        if core.getKeyPressList("q") and self.position[0] > 0:
            self.position = (self.position[0] + -self.vitesse, self.position[1])


    def getPosX(self):
        return self.position[0]
