import pygame

from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageMenu:
    def __init__(self):  # constructeur
        self.couleur = (0,0,0)

        self.posbp = (420-(150/2),300-25)
        self.posbp1 = (420-(140/2),375-25)
        self.posbp2 = (420-(270/2),450-25)
        self.posbp3 = (420-(190/2),525-25)
        self.posbp4 = (30,570)

        self.bp = Bouton1(self.posbp[0], self.posbp[1], Etat.CHARGEMENT,True,"./Image/Template.png",(150,50))
        self.bp1 = Bouton1(self.posbp1[0], self.posbp1[1], Etat.SKIN,True,"./Image/Template.png",(140,50))
        self.bp2 = Bouton1(self.posbp2[0], self.posbp2[1],Etat.COM,True,"./Image/Template.png",(270,50))
        self.bp3 = Bouton1(self.posbp3[0], self.posbp3[1],Etat.DESTROY,True,"./Image/Template.png",(190,50))
        self.bp4 = Bouton1(self.posbp4[0], self.posbp4[1], Etat.LEADERBOARD, True, "./Image/Template.png", (275, 50))


    def update(self):
        self.mouse = pygame.mouse.get_pos()

        if not core.memory("TexTitre").ready:
            core.memory("TexTitre").load()
        core.memory("TexTitre").show()

        core.Draw.text(self.couleur, 'Space Invader ', (165, 80), 40, "./Font/8-BIT WONDER.TTF", False)

        self.bp.show()
        self.bp.updateRect()
        core.Draw.text(self.couleur, 'Jouer ', (self.posbp[0], self.posbp[1]-13), 20, "./Font/8-BIT WONDER.TTF", False)
        self.bp1.show()
        self.bp1.updateRect()
        core.Draw.text(self.couleur, 'Skin ', (self.posbp1[0]+7, self.posbp1[1]-13),20,"./Font/8-BIT WONDER.TTF",False)
        self.bp2.show()
        self.bp2.updateRect()
        core.Draw.text(self.couleur, 'Commandes ', (self.posbp2[0]+5, self.posbp2[1]-13),20,"./Font/8-BIT WONDER.TTF",False)
        self.bp3.show()
        self.bp3.updateRect()
        core.Draw.text(self.couleur, 'Quitter ', (self.posbp3[0]+5, self.posbp3[1]-13),20,"./Font/8-BIT WONDER.TTF",False)
        self.bp4.show()
        self.bp4.updateRect()
        core.Draw.text(self.couleur, 'LEADERBOARD ', (self.posbp4[0] + 5, self.posbp4[1] - 13), 20,
                       "./Font/8-BIT WONDER.TTF", False)

