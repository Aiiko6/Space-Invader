import pygame

from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageMenu:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)

        self.bp = Bouton1(300, 200, Etat.CHARGEMENT,True,"./Image/Play.png",(225,75))
        self.bp1 = Bouton1(300, 300, Etat.OPTION)
        self.bp2 = Bouton1(300, 400,Etat.COM)
        self.bp3 = Bouton1(300, 500,Etat.DESTROY)
        self.bp4 = Bouton1(400, 500, Etat.LEADERBOARD)


    def update(self):
        self.mouse = pygame.mouse.get_pos()

        if not core.memory("TexTitre").ready:
            core.memory("TexTitre").load()
        core.memory("TexTitre").show()

        self.bp.show()
        self.bp.updateRect()
        self.bp1.show()
        self.bp1.update()
        core.Draw.text(self.couleur, 'Parametres ', (340, 280))
        self.bp2.show()
        self.bp2.update()
        core.Draw.text(self.couleur, 'Commandes ', (340, 380))
        self.bp3.show()
        self.bp3.update()
        core.Draw.text(self.couleur, 'Quitter ', (340, 480))

        self.bp4.show()
        self.bp4.update()
