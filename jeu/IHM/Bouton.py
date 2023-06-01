import core


class Bouton:
    def __init__(self, coordX, coordY, Visible=True, URL=""):  # constructeur
        self.Adresse = URL
        self.visible = Visible
        self.couleur = (255, 255, 255)
        self.mass = 20
        self.position = (coordX, coordY)
        self.positionImage = (coordX - 50/2 , coordY - 50/2)
        self.Skin = core.Texture(URL, self.positionImage, 0, (50, 50))
        self.startMenu = 1

    def show(self):
        if self.visible:
            if self.Adresse == "":
                core.Draw.circle(self.couleur, self.position, self.mass)
            else:
                if not self.Skin.ready:
                    self.Skin.load()
                self.Skin.show()
