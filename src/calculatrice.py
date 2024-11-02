from tkiteasy1 import *
class calculette:
    def __init__(self):
        self.g=ouvrirFenetre(400,600)
        self.touche={"0":(133,520),"=":(266,520),"1":(80,440),"2":(160,440),"3":(240,440),"+":(320,440),"4":(80,360),"5":(160,360),"6":(240,360),"-":(320,360),"7":(80,280),"8":(160,280),"9":(240,280),"x":(320,280),"AC":(100,200),"DEL":(200,200),"/":(300,200)}
        self.interface()
        self.entree = ""
    def interface(self):
        self.g.dessinerRectangle(0,0,400,600,"pink")
        self.g.dessinerRectangle(30,30,340,120,"grey")
        for touche in self.touche:
            (x,y)=self.touche[touche]
            self.g.dessinerDisque(x,y,30,"blue")
            self.g.afficherTexte(touche,x,y,"white",18)
        self.g.actualiser()

    def resultat(self, resultat):
        self.g.dessinerRectangle(30, 30, 340, 120, "grey")  # Efface l'écran
        self.g.afficherTexte(str(resultat), 200, 70, "black", 24)
        self.g.actualiser()

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

    def initcalcul(self):
        chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.entree = ""
        operation = None
        resultat = 0
        recup = False

        while recup == False:
            nombre = self.recupererchiffre()
            if str(nombre) in chiffres:
                self.entree += nombre
                self.resultat(self.entree)

            elif nombre == "+" or nombre == "-" or nombre == "x" or nombre == "/":
                if self.entree is not None:
                    resultat = int(self.entree)
                    operation = nombre
                    self.entree += operation  # Ajoute l'opération à l'affichage
                    self.resultat(self.entree)  # Affiche l'opération en cours
                    self.entree = ""

            elif nombre == "=":
                if operation is not None and self.entree is not None:
                    resultat = self.calcul(int(resultat), int(self.entree), operation)
                    self.resultat(resultat)
                    self.entree = str(resultat)
                    operation = None


            elif nombre == "AC":
                self.entree = ""
                resultat = 0
                operation = None
                self.resultat(0)

            elif nombre == "DEL":
                self.entree = self.entree[:-1]
                self.resultat(self.entree if self.entree is not None else 0)

    def calcul(self, nombre1, nombre2, operation):
        if operation == "+":
            return nombre1 + nombre2

        if operation == "-":
            return nombre1 - nombre2

        if operation == "x":
            return nombre1*nombre2

        if operation == "/":
            if nombre2 != 0:
                return nombre1 / nombre2
            else:
                return "Erreur"






a=calculette()
a.initcalcul()

