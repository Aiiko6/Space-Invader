from pygame import Vector2

import core


class BarreAmelioration:
    def __int__(self,coordX,coordY):
        self.position = Vector2(coordX,coordY)
        self.stat = 1
        self.textureURL = "Barredame"

    def show(self):
        if not core.memory(self.textureURL + str(self.stat)).ready:
            core.memory(self.textureURL + str(self.stat)).load()
        core.memory(self.textureURL + str(self.stat)).pos = self.position
        core.memory(self.textureURL + str(self.stat)).show()

