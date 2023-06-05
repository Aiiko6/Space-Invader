import sys

import pygame

import core
from jeu.Etat import Etat
from jeu.IHM.FrontMontant import frontMontant
from jeu.IHM.PageChargement import PageChargement
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
    core.memory("PageChargement", PageChargement())
    #Declaration variable Partie
    core.memory("maPartie", Partie())
    core.WINDOW_SIZE = [800, 600]
    global background
    background = core.Texture("./Image/Fond_ecran800.png", (0, 0), 0, core.WINDOW_SIZE)

    core.memory("TextureVaisseau", core.Texture('./Image/Vaisseau.png', (0, 0), 0, (50, 50)))
    core.memory("Barredame4", core.Texture('./Image/Barredame4.png', (0, 0), 0, (100, 19)))
    core.memory("Barredame3", core.Texture('./Image/Barredame3.png', (0, 0), 0, (100, 19)))
    core.memory("Barredame2", core.Texture('./Image/Barredame2.png', (0, 0), 0, (100, 19)))
    core.memory("Barredame1", core.Texture('./Image/Barredame1.png', (0, 0), 0, (100, 19)))

    core.memory("maPartie").addJoueur()
    core.memory("maPartie").addMissile()

    core.memory("previous_mouse_state", False)
    core.memory("current_mouse_state", False)

    core.memory("gestionFront",frontMontant())


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

    if core.memory('etat') == Etat.DESTROY:
        pygame.quit()
        sys.exit()

    if core.memory('etat') == Etat.CHARGEMENT:
        core.memory("PageChargement").update()




core.main(setup,run)


