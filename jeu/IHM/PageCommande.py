from jeu import core
from jeu.Etat import Etat
from jeu.IHM.Bouton1 import Bouton1


class PageCommande:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)

        self.bp = Bouton1(300, 500,Etat.MENU)


    def update(self):
        self.mouse = core.getMouseLocation()
        core.Draw.text(self.couleur, 'Commande:', (300, 10))
        core.Draw.text(self.couleur, 'Gauche: q ', (340, 180))
        core.Draw.text(self.couleur, 'Droite: d ', (340, 280))
        core.Draw.text(self.couleur, 'Tirer: espace', (340, 380))
        self.bp.show()
        self.bp.update()
        core.Draw.text(self.couleur, 'Retour ', (340, 480))

