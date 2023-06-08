from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageCommande:
    def __init__(self):  # constructeur
        self.couleur = (0, 0, 0)
        self.posbp3 = (400 - (190 / 2), 525 - 25)
        self.bp3 = Bouton1(self.posbp3[0], self.posbp3[1], Etat.MENU, True, "./Image/Template.png", (190, 50))



    def update(self):
        self.mouse = core.getMouseLocation()

        if not core.memory("TexTitre").ready:
            core.memory("TexTitre").load()
        core.memory("TexTitre").show()

        core.Draw.text(self.couleur, 'Commande', (200, 80),40, "./Font/8-BIT WONDER.TTF", False)
        core.Draw.text((255, 255, 255), 'Gauche q ', (300, 230),20, "./Font/8-BIT WONDER.TTF", False)
        core.Draw.text((255, 255, 255), 'Droite d ', (300, 270),20, "./Font/8-BIT WONDER.TTF", False)
        core.Draw.text((255, 255, 255), 'Tirer espace', (300, 310),20, "./Font/8-BIT WONDER.TTF", False)
        core.Draw.text((255, 255, 255), 'Amelioration e', (300, 350), 20, "./Font/8-BIT WONDER.TTF", False)
        core.Draw.text((255, 255, 255), 'Pause ECHAPE', (300, 390), 20, "./Font/8-BIT WONDER.TTF", False)


        self.bp3.show()
        self.bp3.updateRect()
        core.Draw.text(self.couleur, 'Retour ', (self.posbp3[0] + 5, self.posbp3[1] - 13), 20,
                       "./Font/8-BIT WONDER.TTF", False)

