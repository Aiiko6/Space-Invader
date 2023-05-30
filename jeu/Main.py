import core
from jeu.Etat import Etat
from jeu.IHM.PageMenu import PageMenu
from jeu.IHM.PauseMenu import PauseMenu
from jeu.Partie import Partie

couleur = (0,0,0)

def setup():
    core.fps = 60
    core.memory("etat", Etat.MENU)
    core.memory("PageMenu",PageMenu())
    core.memory("PausePage", PauseMenu())

    #Declaration variable Partie
    core.memory("maPartie", Partie())
    core.WINDOW_SIZE = [800, 600]


    core.memory("maPartie").addJoueur()
    core.memory("maPartie").addMissile()

def run():
    core.cleanScreen()

    if core.memory('etat') == Etat.MENU:
        core.memory("PageMenu").update()

    if core.memory('etat') == Etat.PAUSE:
        core.memory("PausePage").update()

    if core.memory('etat') == Etat.JEU:
        #print('jeu')
        core.memory("maPartie").addEnnemis()
        core.memory("maPartie").show()
        core.memory("maPartie").update()




core.main(setup,run)


