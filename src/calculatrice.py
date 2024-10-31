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



    def calcul(self):
        return None

a=calculette()
a.fonc()
