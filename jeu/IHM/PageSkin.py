import pygame
from pygame import Vector2

from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton import Bouton


class PageSkin:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)

        self.bp3 = Bouton(300, 500)
        self.Flechedroite = Bouton(141, 275, True, "./Image/Fleche_droite.png")
        self.FlecheGauche = Bouton(657, 275, True, "./Image/Fleche_gauche.png")
        self.mouse = pygame.mouse.get_pos()
        self.massCursor = 2
        self.startMenu = 1
        self.selector = 0
        self.skinURLList = ['./Image/Ship.png', './Image/Vaisseau.png','./Image/Vaisseau2.png','./Image/Vaisseau3.png']
        self.skinTailleList = [(100, 100), (150, 100), (100, 100),(100, 100)]

    def update(self):

        self.mouse = core.getMouseLocation()

        self.bp3.show()
        self.Flechedroite.show()
        self.FlecheGauche.show()

        self.skinURLChoix = core.Texture(self.skinURLList[self.selector - 1],
                                         (400 - (self.skinTailleList[self.selector][0]/2), 300 - (self.skinTailleList[self.selector][1]/2)), 0,
                                         self.skinTailleList[self.selector])

        core.memory("TextureVaisseau", core.Texture(self.skinURLList[self.selector - 1], (0, 0), 0, (self.skinTailleList[self.selector][0] - 50, self.skinTailleList[self.selector][1] - 50)))

        if not self.skinURLChoix.ready:
            self.skinURLChoix.load()
        self.skinURLChoix.show()

        core.Draw.text(self.couleur, 'Retour ', (340, 480))

        if (self.startMenu == 0) or (not core.getMouseLeftClick()):
            self.startMenu = 0
            if core.getMouseLeftClick() and self.distanceCheck(self.bp3):
                self.startMenu = 1
                core.memory('etat', Etat.OPTION)
            if core.getMouseLeftClick() and self.distanceCheck(self.Flechedroite):
                self.startMenu = 1
                self.selector = self.selector + 1
                if self.selector > (len(self.skinURLList) - 1):
                    self.selector = 0
            if core.getMouseLeftClick() and self.distanceCheck(self.FlecheGauche):
                self.startMenu = 1
                self.selector = self.selector - 1
                if self.selector < 0:
                    self.selector = (len(self.skinURLList) - 1)

    def distanceCheck(self, bouton):
        pos1 = Vector2(self.mouse)
        pos2 = Vector2(bouton.position)
        distance = pos1 - pos2
        if self.massCursor + bouton.mass > distance.length():
            return True
        else:
            return False
