import core
from jeu.IHM.BarreAmelioration import BarreAmelioration


class MenuAchat:
    def __init__(self):  # constructeur
        self.couleur = (255, 255, 255)
        self.mouse = core.getMouseLocation()
        self.massCursor = 2
        self.startMenu = 1
        core.memory("TextureAchat", core.Texture('./Image/MenuAchat.png', (65, 50), 0, (650, 500)))
        self.position = core.memory("TextureAchat").pos
        self.money = 0
        self.barreameMuni = BarreAmelioration()
        self.vitesseVaisseau = BarreAmelioration()
        self.nbTir = BarreAmelioration()
        self.vitesseMunition = BarreAmelioration()

    def affichageMenu(self):

        if not core.memory("TextureAchat").ready:
            core.memory("TextureAchat").load()
        core.memory("TextureAchat").show()

        core.Draw.text((255,255,255), str(core.memory("maPartie").money), (520 + self.position[0] - 25 * (len(str(self.money))), 355 + self.position[1]),50)

