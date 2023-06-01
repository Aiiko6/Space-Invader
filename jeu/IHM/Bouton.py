import core


class Bouton:
    def __init__(self, coordX, coordY, Visible=True, URL=""):  # constructeur
        self.Adresse = URL
        self.visible = Visible
        self.couleur = (255, 255, 255)
        self.position = (coordX, coordY)
        self.mass = 20
        self.Skin = core.Texture(URL, self.position, 0, (50, 50))
        self.startMenu = 1

    def show(self):
        if self.visible:
            if self.Adresse == "":
                core.Draw.circle(self.couleur, self.position, self.mass)
            else:
                if not self.Skin.ready:
                    self.Skin.load()
                self.Skin.pos = self.position
                self.Skin.show()