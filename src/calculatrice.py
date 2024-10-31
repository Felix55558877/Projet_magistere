from tkiteasy import *

class calculette:
    def __init__(self):
        self.g=ouvrirFenetre(400,600)
        self.touche={"0":(133,520),"=":(266,520),"1":(80,440),"2":(160,440),"3":(240,440),"+":(320,440),"4":(80,360),"5":(160,360),"6":(240,360),"-":(320,360),"7":(80,280),"8":(160,280),"9":(240,280),"x":(320,280),"AC":(100,200),"DEL":(200,200),"/":(300,200)}
        self.interface()
    def interface(self):
        self.g.dessinerRectangle(0,0,400,600,"pink")
        self.g.dessinerRectangle(30,30,340,120,"grey")
        for touche in self.touche:
            (x,y)=self.touche[touche]
            self.g.dessinerDisque(x,y,30,"blue")
            self.g.afficherTexte(touche,x,y,"white",18)
        self.g.actualiser()


    def fonc(self):
        self.recupererchiffre()

    def recupererchiffre(self):
        recup=False
        while recup==False:
            c=self.g.recupererClic()
            if c!=None:
                (x2, y2) = (c.x,c.y)
                for touche in self.touche:
                    (x, y) = self.touche[touche]
                    if abs(x2 - x) <= 30 and abs(y2 - y) <= 30:
                        recup = True
                        choix = touche
        return choix

    def initgra(self):
        return None
    def initchiffre(self):
        chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        entree = ""
        recup = False
        while recup == False:
            nombre = self.recupererchiffre()
            if str(nombre) in chiffres:
                entree += nombre

    def creechiffre(self):
        chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        entree = ""
        recup = False
        while recup == False:
            nombre = self.recupererchiffre()
            if str(nombre) in chiffres:
                entree += nombre
            if nombre == "+":
                return (int(entree), "+")
            if nombre == "-":
                return (int(entree), "-")
            if nombre == "x":
                return (int(entree), "x")
            if nombre == "AC":
                return (int(entree), "AC")
            if nombre == "DEL":
                return (int(entree), "DEL")
            if nombre == "/":
                return (int(entree), "/")
    def initcalcul(self):
        chiffres = ["0","1","2","3","4","5","6","7","8","9"]
        entree = ""
        recup = False
        while recup == False:
            nombre = self.recupererchiffre()
            if str(nombre) in chiffres:
                entree += nombre
            if nombre == "+":
                return self.calcul(int(entree),"+")
            if nombre == "-":
                return self.calcul(int(entree), "-")
            if nombre == "x":
                return self.calcul(int(entree),"x")
            if nombre == "AC":
                return self.calcul(int(entree),"AC")
            if nombre == "DEL":
                entree = pop.entree
            if nombre == "/":
                return self.calcul(int(entree),"/")





    def calcul(self, nombre, operation):
        if operation == "+":
            nv_nombre, operation2 = self.creechiffre()
            resultat = nombre + int(nv_nombre)
            return self.calcul(resultat,operation2)

        if operation == "-":
            nv_nombre, operation2 = self.creechiffre()
            resultat = nombre - int(nv_nombre)
            return self.calcul(resultat, operation2)

        if operation == "x":
            nv_nombre, operation2 = self.creechiffre()
            resultat = nombre * int(nv_nombre)
            return self.calcul(resultat, operation2)

        if operation == "division":
            nv_nombre, operation2 = self.creechiffre()
            resultat = nombre / int(nv_nombre)
            return self.calcul(resultat, operation2)

        if operation == "DEL":
            nv_nombre = str(nombre)
            nv_nombre1 = pop.nv_nombre
            return self.calcul()
        if operation == "resultat":
            return nombre






a=calculette()
a.fonc()

