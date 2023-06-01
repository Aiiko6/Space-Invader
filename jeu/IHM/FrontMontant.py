import pygame
from pygame import mouse

import core


class frontMontant:
    current_mouse_state = ""
    previous_mouse_state = ""
    pass

    def update(self):
        # detection de l'état de la souris
        self.current_mouse_state = mouse.get_pressed()[0]

        # Détection du front montant
        if (self.current_mouse_state==True) and (self.previous_mouse_state == False):
            self.previous_mouse_state = self.current_mouse_state
            return True


        # Mise à jour de l'état précédent de la souris
        self.previous_mouse_state = self.current_mouse_state
        return False
