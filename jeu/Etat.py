from enum import Enum


class Etat(Enum):
    MENU = 0
    JEU = 1
    GAMEOVER = 2
    SCORE = 3
    PAUSE = 4
    OPTION = 5