import pygame

from jeu import core
from jeu.Etat import Etat

from jeu.IHM.Bouton1 import Bouton1


class PageSauvegarde:
    def __init__(self):  # constructeur
        self.couleur = (255,255,255)
        self.score = ""
        self.bp11 = Bouton1(150,200,"")
        self.bp12 = Bouton1(150, 400, "")

        self.bp21 = Bouton1(300, 200, "")
        self.bp22 = Bouton1(300, 400, "")

        self.bp31 = Bouton1(450, 200, "")
        self.bp32 = Bouton1(450, 400, "")

        self.bpSauvegarde = Bouton1(570,320,"")

        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                     "u", "v", "w", "x", "y", "z"]

        self.lettres = [self.alphabet[0],self.alphabet[0],self.alphabet[0]]
        self.pointeurs = [0,0,0]

        self.nom= ""


    def update(self):

        self.mouse = pygame.mouse.get_pos()
        core.Draw.text(self.couleur, 'Sauvegarde: ', (300, 10))
        self.bp11.show()
        if self.bp11.update1():
            self.augmenterLettre(0)
            print(self.lettres[0])

        self.bp21.show()
        if self.bp21.update1():
            self.augmenterLettre(1)
            print(self.lettres[1])

        self.bp31.show()
        if self.bp31.update1():
            self.augmenterLettre(2)
            print(self.lettres[2])


        self.bp12.show()
        if self.bp12.update1():
            self.diminuerLettre(0)
            print(self.lettres[0])

        self.bp22.show()
        if self.bp22.update1():
            self.diminuerLettre(1)

        self.bp32.show()
        if self.bp32.update1():
            self.diminuerLettre(2)

        core.Draw.text(self.couleur, str(self.lettres[0]), (150, 300))
        core.Draw.text(self.couleur, str(self.lettres[1]), (300, 300))
        core.Draw.text(self.couleur, str(self.lettres[2]), (450, 300))

        self.bpSauvegarde.show()
        core.Draw.text(self.couleur, "Sauvegarder", (600, 300))
        if self.bpSauvegarde.update1():
            self.compilerNom()





    def augmenterLettre(self,nb_lettre):
        if self.pointeurs[nb_lettre] !=25:
            self.pointeurs[nb_lettre] = self.pointeurs[nb_lettre] + 1

        else:
            self.pointeurs[nb_lettre] = 0
        self.lettres[nb_lettre] = self.alphabet[self.pointeurs[nb_lettre]]

    def diminuerLettre(self, nb_lettre):
        if self.pointeurs[nb_lettre] !=0:
            self.pointeurs[nb_lettre] = self.pointeurs[nb_lettre] - 1

        else:
            self.pointeurs[nb_lettre] = 25
        self.lettres[nb_lettre] = self.alphabet[self.pointeurs[nb_lettre]]

    def compilerNom(self):
        self.nom = self.lettres[0] + self.lettres[1] + self.lettres[2]
        print(self.nom)

        core.memory("gestionFichier").ecrireFichier(self.nom +", " + str(self.score)) #Ecriture dans le fichier
        core.memory("etat",Etat.MENU)


    def setScore(self):
        self.score = core.memory("maPartie").get_score() + core.memory("maPartie").get_money()- (core.memory("maPartie").get_nombreCoup()/2)




