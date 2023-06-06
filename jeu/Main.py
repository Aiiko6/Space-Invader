import sys

import pygame

from jeu.Etat import Etat
from jeu.Gestionfichier import GestionFichier
from jeu.IHM.FrontMontant import frontMontant
from jeu.IHM.PageChargement import PageChargement
from jeu.IHM.PageCommande import PageCommande
from jeu.IHM.PageGameOver import PageGameOver
from jeu.IHM.PageGraphique import PageGraphique
from jeu.IHM.PageLeaderboard import PageLeaderBoard
from jeu.IHM.PageMenu import PageMenu
from jeu.IHM.PageOption import PageOption
from jeu.IHM.PageSauvegarde import PageSauvegarde
from jeu.IHM.PageSkin import PageSkin
from jeu.IHM.PauseMenu import PauseMenu
from jeu.Leaderboard.Classement import Classement
from jeu.Partie import Partie
from jeu import core

def setup():

    core.fps = 60
    core.memory("etat", Etat.MENU)
    core.memory("PageMenu", PageMenu())
    core.memory("PausePage", PauseMenu())
    core.memory("OptionPage", PageOption())
    core.memory("PageGameOver", PageGameOver())
    core.memory("PageCommande", PageCommande())
    core.memory("GraphiPage", PageGraphique())
    core.memory("SkinPage", PageSkin())
    core.memory("PageChargement", PageChargement())
    core.memory("PageSauvegarde", PageSauvegarde())
    core.memory("PageLeaderBoard", PageLeaderBoard())
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

    core.memory("textureEnemy1", core.Texture("./Image/Enemy.png", (0, 0), 0, (50, 50)))
    core.memory("textureEnemy2", core.Texture("./Image/Enemy2.png", (0, 0), 0, (50, 50)))
    core.memory("textureEnemy3", core.Texture("./Image/Enemy3.png", (0, 0), 0, (50, 50)))
    core.memory("textureEnemy4", core.Texture("./Image/Enemy4.png", (0, 0), 0, (50, 50)))

    core.memory("TexTitre", core.Texture("./Image/Titre.png", (150, 50), 0, (500, 100)))



    core.memory("maPartie").addJoueur()
    core.memory("maPartie").addMissile()

    core.memory("previous_mouse_state", False)
    core.memory("current_mouse_state", False)

    core.memory("gestionFront", frontMontant())


    #Classement
    core.memory("gestionFichier",GestionFichier("../temp.txt"))
    core.memory("Classement", Classement())
    core.memory("Classement",).getFile()


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

    if core.memory('etat') == Etat.SAUVEGARDE:
        core.memory("PageSauvegarde").update()

    if core.memory('etat') == Etat.LEADERBOARD:
        core.memory("PageLeaderBoard").update()




core.main(setup, run)


