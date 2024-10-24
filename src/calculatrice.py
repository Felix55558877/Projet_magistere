from tkiteasy import *

class calculette:
    def __init__(self):
        self.g=ouvrirFenetre(400,800)
        self.g.attendreClic()
        self.touche = {}

    def initgra(self):
        return None



    def addition(self,nombre):
        a = True
        chiffre = ""
        while a :
            touche = self.recupererChiffre()
            if touche == "exe" :
                break
            chiffre += str(touche)
        number = int(nombre)
        return nombre + number


    def soustraction(self,nombre):
        a = True
        chiffre = ""
        while a :
            touche = self.recupererChiffre()
            if touche == "exe" :
                break
            chiffre += str(touche)
        number = int(nombre)
        return nombre - number

    def multiplication(self,nombre):
        a = True
        chiffre = ""
        while a :
            touche = self.recupererChiffre()
            if touche == "exe" :
                break
            chiffre += str(touche)
        number = int(nombre)
        return nombre * number

    def calcul(self,nombre,operation):
        if operation == "addition":
            a = True
            chiffre = ""
            while a:
                clic = self.recuperchiffre()
                if clic == addition or clic == soustraction or clic == division or clic == multiplication :
                    return self.str(clic)(number+nombre)
                chiffre.add(clic)
                number = int(chiffre)
        if operation == "soustraction":
            a = True
            chiffre = ""
            while a:
                if clic == addition or clic == soustraction or clic == division or clic == multiplication :
                    return self.str(clic)(number-nombre)
                clic = None
                chiffre.add(clic)
                number = int(chiffre)
        if operation == "multpilication":
            a = True
            chiffre = ""
            while a:
                if clic == addition or clic == soustraction or clic == division or clic == multiplication :
                    return self.str(clic)(number*nombre)
                clic = None
                chiffre.add(clic)
                number = int(chiffre)
        if operation == "division":
            a = True
            chiffre = ""
            while a:
                if clic == addition or clic == soustraction or clic == division or clic == multiplication :
                    return self.str(clic)(number/nombre)
                clic = None
                chiffre.add(clic)
                number = int(chiffre)
        if operation == "supprimer" :
            nv_nombre = str(nombre)
            nv_nombre1 = pop.nv_nombre
            return self.calcul()
        if operation == "resultat":
            return nombre