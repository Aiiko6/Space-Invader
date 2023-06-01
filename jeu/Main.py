import pygame

import core
from jeu.Etat import Etat
from jeu.IHM.PageCommande import PageCommande
from jeu.IHM.PageGameOver import PageGameOver
from jeu.IHM.PageGraphique import PageGraphique
from jeu.IHM.PageMenu import PageMenu
from jeu.IHM.PageOption import PageOption
from jeu.IHM.PageSkin import PageSkin
from jeu.IHM.PauseMenu import PauseMenu
from jeu.Partie import Partie

def setup():

    core.fps = 60
    core.memory("etat", Etat.MENU)
    core.memory("PageMenu",PageMenu())
    core.memory("PausePage", PauseMenu())
    core.memory("OptionPage", PageOption())
    core.memory("PageGameOver",PageGameOver())
    core.memory("PageCommande", PageCommande())
    core.memory("GraphiPage", PageGraphique())
    core.memory("SkinPage", PageSkin())
    #Declaration variable Partie
    core.memory("maPartie", Partie())
    core.WINDOW_SIZE = [800, 600]
    global background
    background = core.Texture("./Image/Fond_ecran800.png", (0, 0), 0, core.WINDOW_SIZE)
    core.memory("TextureVaisseau", core.Texture('./Image/Vaisseau.png', (0, 0), 0, (50, 50)))

    core.memory("maPartie").addJoueur()
    core.memory("maPartie").addMissile()


def run():
    global background
    core.cleanScreen()

    if not background.ready:
        background.load()
    background.show()


    if core.memory('etat') == Etat.MENU:
        core.memory("PageMenu").update()

    if core.memory('etat') == Etat.PAUSE:
        core.memory("PausePage").update()

    if core.memory('etat') == Etat.OPTION:
        core.memory("OptionPage").update()

    if core.memory('etat') == Etat.GRAPHI:
        core.memory("GraphiPage").update()

    if core.memory('etat') == Etat.SKIN:
        core.memory("SkinPage").update()

    if core.memory('etat') == Etat.JEU:
        #print('jeu')
        core.memory("maPartie").addEnnemis()
        core.memory("maPartie").show()
        core.memory("maPartie").update()

    if core.memory('etat') == Etat.GAMEOVER:
        core.memory("PageGameOver").update()

    if core.memory('etat') == Etat.COM:
        core.memory("PageCommande").update()



core.main(setup,run)


