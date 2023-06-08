


class GestionFichier():
    def __init__(self,nom):
        self.nom = nom
        self.file = open(self.nom,"a")
        self.file.close()




    def ecrireFichier(self,texte):
        self.file = open(self.nom,"a")
        self.file.write(texte + "\n")
        self.file.close()

    def compterLigne(self):
        with open(self.nom, 'r') as fp:
            lines = len(fp.readlines())
            print("nb ligne: " +str(lines))
            fp.close()
            return lines



    def lireLigne(self,num):
        file = open(self.nom, "r")
        l = [file.read().replace("\n", ";")]    #Supprime les retours à la ligne
        file.close()
        texte = ''.join(l)          #Convertie la liste en string
        res = texte.split(';')      #Separe la chaine avec le séparateur ";"
        return res[num]

