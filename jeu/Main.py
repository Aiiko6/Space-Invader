import core
from jeu.Etat import Etat
from jeu.IHM.PageMenu import PageMenu
from jeu.Partie import Partie

couleur = (255,255,255)

def setup():
    core.fps = 60

    core.memory("etat", Etat.MENU)
    core.memory("PageMenu",PageMenu())

    #Declaration variable Partie
    core.memory("maPartie", Partie())
    core.WINDOW_SIZE = [800, 600]


    core.memory("maPartie").addJoueur()
    core.memory("maPartie").addMissile()

def run():
    core.cleanScreen()

    if core.memory('etat') == Etat.MENU:
        core.memory("PageMenu").update()
        #print('menu')

        if core.getMouseLeftClick():
            core.memory('etat',Etat.JEU)

    if core.memory('etat') == Etat.JEU:
        #print('jeu')
        core.memory("maPartie").addEnnemis()
        core.memory("maPartie").show()
        core.memory("maPartie").update()

        if core.getMouseRightClick():
            core.memory('etat',Etat.MENU)





core.main(setup,run)


