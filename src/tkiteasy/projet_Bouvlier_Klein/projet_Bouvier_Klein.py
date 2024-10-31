import random
from tkiteasy import *
import time
from math import *
import time

dimx = 600
dimy = 600
NBP = 5
VALMAX = 10
LIMITE = -20
TEMPS = 30

class Projet():
    def __init__(self):
        self.dimx = dimx
        self.dimy = dimy
        self.g = ouvrirFenetre(self.dimx, self.dimy)
        self.NBP = NBP
        self.TEMPS = 1.25 * self.NBP
        self.nbauto = NBP
        self.limitauto = LIMITE
        self.VALMAX = VALMAX
        self.limit = LIMITE
        self.poubelle = []
        self.couleur = {(-1): ["rose"], (-3): ["bleuviolet"], (-5): ["violet pâlerouge"], (-8): ["bleu ardoise foncé"],(-10): ["bleu royal"]}
        self.dicjet = {}
        self.score = 0
        self.score2 = 0
        self.poid = 0
        self.dico = {}
        self.dicoval = {}
        self.dijet()
        self.menu()
    #On premier on trouve toutes les fonctions de menus (assez long)
    def menujeu(self): #affichage du menu on l'on choisi le menu
        button_largeur = 0.5 * self.dimx
        button_hauteur = 0.3 * self.dimy
        button_x = (self.dimx - button_largeur) / 2
        button_y = (self.dimy - button_hauteur) / 2
        play_y = (self.dimy - button_hauteur) * (1 / 3)
        image = self.g.afficherImage(0, 0, "image_menu_jeu.jpg", self.dimx, self.dimy)
        rect1 = self.g.dessinerRectangle(button_x / 2, button_y, button_largeur / 2, button_hauteur / 2, "slateblue")
        rect2 = self.g.dessinerRectangle(2.5 * button_x, button_y, button_largeur / 2, button_hauteur / 2,"darkmagenta")
        texte_joueur1 = self.g.afficherTexte("1 joueur", button_x / 2 + 0.25 * button_largeur,button_y + 0.25 * button_hauteur)
        texte_joueur2 = self.g.afficherTexte("2 joueurs", 2.5 * button_x + 0.25 * button_largeur,button_y + 0.25 * button_hauteur)
        sol = self.g.afficherTexte("Jeu optimal", self.dimx / 2, self.dimy * (7 / 8), "orchid")
        regles = self.g.afficherTexte("Afficher les regles", self.dimx / 2, self.dimy * (1 / 8),"blue")
        choisir = self.g.afficherTexte("Changer les parametres", self.dimx / 2, self.dimy * (2 / 8), "royalblue")
        change = self.g.afficherTexte("Regénérer jeton",self.dimx/2, self.dimy*(2/3),"purple")
        fermé = self.g.dessinerDisque(20, self.dimy - 20, 15, "red")

        while True:
            clic = self.g.attendreClic()
            objetclic = self.g.recupererObjet(clic.x, clic.y)
            if objetclic == rect1 or objetclic == texte_joueur1 or objetclic == rect2 or objetclic == texte_joueur2 or objetclic == regles or objetclic == sol or objetclic == change or objetclic == fermé or objetclic == choisir:
                self.g.supprimer(rect1), self.g.supprimer(rect2),self.g.supprimer(texte_joueur1), self.g.supprimer(texte_joueur2),self.g.supprimer(regles), self.g.supprimer(sol), self.g.supprimer(change), self.g.supprimer(fermé), self.g.supprimer(choisir)
                if objetclic == rect1 or objetclic == texte_joueur1:
                    return self.Grafj2(1)
                if objetclic == rect2 or objetclic == texte_joueur2:
                    return self.Grafj2(2)
                if objetclic == regles:
                    return self.Regles()
                if objetclic == change:
                    self.dijet()
                    self.menujeu()
                if objetclic == sol:
                    return self.menuopti()
                if objetclic == choisir:
                    return self.mode()
                if objetclic == fermé:
                    self.g.fermerFenetre()


    def menu(self): #Page d'acceuil du jeu
        button_largeur = 0.5 * self.dimx /2.8
        button_hauteur = 0.3 * self.dimy/3
        button_x = (self.dimx - button_largeur) / 2
        button_y = (self.dimy - button_hauteur) / 2
        play_y = (self.dimy - button_hauteur) * (0.98 / 2)-5
        # Dessiner le bouton Play et image
        image = self.g.afficherImage(0, 0, "image_arcade.png", self.dimx, self.dimy)
        rect = self.g.dessinerRectangle(button_x, play_y, button_largeur, button_hauteur, "palevioletred")
        play = self.g.afficherTexte("Play", self.dimx / 2, play_y + button_hauteur / 2,"purple")
        fermé = self.g.dessinerDisque(20,self.dimy-20,15,"red")
        while True:
            clic = self.g.attendreClic()
            objetclic = self.g.recupererObjet(clic.x, clic.y)
            if objetclic == rect or objetclic == play:
                self.g.supprimer(rect),self.g.supprimer(play),self.g.supprimer(image),self.g.supprimer(fermé)
                return self.menujeu() #on appelle le second menu
            if objetclic ==  fermé:
                self.g.fermerFenetre()

    def menuopti(self): #Menu pour les jeux automatiques
        poubmen = []
        naif = self.g.afficherTexte("Solution naive", self.dimx/2,self.dimy*(1/3))
        opti =self.g.afficherTexte("Solution intelligente", self.dimx/2,self.dimy*(2/3))
        poubmen.append(naif),poubmen.append(opti)#,poubmen.append(R)
        while True:
            clic = self.g.attendreClic()
            if self.g.recupererObjet(clic.x,clic.y) == naif:
                for x in poubmen:
                    self.g.supprimer(x)
                self.naif()
            if self.g.recupererObjet(clic.x,clic.y) == opti:
                for x in poubmen:
                    self.g.supprimer(x)
                self.resIntelligente()

    def Regles(self): #Menu avec affichage des regles
        P1 = self.g.afficherTexte("Voici le But du jeu:", self.dimx / 2, self.dimy / 9, "darkorchid")
        P2 = self.g.afficherTexte("Choisissez les pièces pour maximiser votre score.", self.dimx / 2,self.dimy * (2 / 9), "darkorchid")
        P3 = self.g.afficherTexte("Chaque pièce a une valeur et une couleur.", self.dimx / 2, self.dimy * (3 / 9),"darkorchid")
        P4 = self.g.afficherTexte("Attention : chaque couleur a une valeur négative.", self.dimx / 2,self.dimy * (4 / 9), "darkorchid")
        P5 = self.g.afficherTexte("Votre objectif : ne pas dépasser la limite de couleur.", self.dimx / 2,self.dimy * (5 / 9), "darkorchid")
        P6 = self.g.afficherTexte("Obtenez le meilleur score en respectant cette contrainte.", self.dimx / 2,self.dimy * (6 / 9), "darkorchid")
        P7 = self.g.afficherTexte("Êtes-vous prêt ? Cliquez sur 'Jouer' pour commencer !", self.dimx / 2,self.dimy * (7 / 9), "darkorchid")
        P8 = self.g.afficherTexte("Retour au menu", self.dimx / 2, self.dimy * (8 / 9), "plum")
        objets_a_supprimer = [P1, P2, P3, P4, P5, P6, P7, P8]
        while True:
            clic = self.g.attendreClic()
            if self.g.recupererObjet(clic.x, clic.y) == P8:
                for i in objets_a_supprimer:
                    self.g.supprimer(i)
                self.menujeu()
                break

    def dijet(self):
        self.dicjet.clear() #on le vide pour evider dempiler plusieurs jetons
        (posx, posy) = self.dim()
        coord = []
        for i in range(len(posy)):
            for j in range(len(posx)):
                coord.append((posx[j], posy[i]))
        for i in range(self.NBP):
            val = random.randint(0, self.VALMAX)
            coul = random.choice([couleur for couleurs in self.couleur.values() for couleur in couleurs])
            self.dicjet[coord[i]] = [val, coul]

    def dim(self):  # Fonction pour renvoyer les positions des jetons ainsi que le rayon
        Ncolonne = ceil(sqrt(self.NBP))
        Nligne = ceil(self.NBP / Ncolonne)
        posx = []
        posy = []
        # Définir la taille de la grille
        taille_x = self.dimx * 2 / 3
        taille_y = self.dimy / 2
        self.rayon = (taille_x / Ncolonne) / 3
        # Calculer les coordonnées x des colonnes pour centrer la grille horizontalement
        for i in range(Ncolonne):
            marche = taille_x / Ncolonne
            x = (self.dimx - taille_x) / 2 + marche * (i + 1) - 0.5 * marche
            posx.append(x)

        # Calculer les coordonnées y des lignes, en commençant depuis le bas
        for v in range(Nligne):
            marche = taille_y / Nligne
            y = taille_y + marche * (v + 1) - 0.5 * marche
            posy.append(y)

        return posx, posy

    def dimaffichage(self):  # fonction qui sert seulement pour creer les dimensions des jetons qui seront affiché pour montrer le cout des couleurs
        posx = []
        posy = []
        taille_x = self.dimx / 6
        taille_y = self.dimy / 2
        self.rayon2 = (taille_x) / 4
        for i in range(1):
            x = taille_x / 2
            posx.append(x)
        # Calculer les coordonnées y des lignes, en commençant depuis le bas
        for v in range(5):
            marche = taille_y / 5
            y = taille_y + marche * (v + 1) - 0.5 * marche
            posy.append(y)
        return (posx, posy)

    def mode(self): #Fonction permettant au joueur de choisir le nombre de jetons mais non abouti pour l'instant
        P1 = self.g.afficherTexte("Choisir la limite", self.dimx / 2, self.dimy * (1 / 3),"blueviolet")
        P2 = self.g.afficherTexte("Choisir le nombre de pieces ", self.dimx / 2, self.dimy * (2 / 3),"blueviolet")
        retour = self.g.afficherTexte("Valider le choix", self.dimx / 2, self.dimy * (4 / 5),"pink")
        self.ajPoub(P1),self.ajPoub(P2),self.ajPoub(retour)
        clic = self.g.attendreClic()
        if self.g.recupererObjet(clic.x, clic.y) == retour:
            self.vider()
            self.dijet()
            self.menujeu()
            return self.menujeu()
        if self.g.recupererObjet(clic.x, clic.y) == P1:
            self.vider()
            P5 = self.g.afficherTexte("Entrez la valeur de la limite", self.dimx / 2, self.dimy * (1 / 3),"magenta")
            R = self.g.afficherTexte("Appuyer sur entrer pour valider", self.dimx / 2, self.dimy * (1 / 6),"magenta")
            self.ajPoub(P5), self.ajPoub(R)
            nombre = ''
            while True:
                touche = self.g.attendreTouche()
                if touche == "Return":
                    break
                try: #On test si le nombre entré peut etre converti en entier
                    entier = int(touche)  # Convertit la touche en entier
                    nombre += str(entier)  # Ajouter l'entier à la chaîne de nombre
                    valeurlim = int(nombre)
                    self.limit = -valeurlim
                except ValueError:
                    er = self.g.afficherTexte("Veuillez entrer un entier valide.", self.dimx / 2, self.dimy / 2,"magenta")
                    self.ajPoub(er)
            P4 = self.g.afficherTexte("La limite est : {}".format(valeurlim), self.dimx / 2, self.dimy * (2 / 3),"magenta")
            self.ajPoub(P4)
            self.g.attendreClic()
            self.vider()
            return self.mode()  # Fin de la fonction mode

        if self.g.recupererObjet(clic.x, clic.y) == P2:
            self.vider()
            P7 = self.g.afficherTexte("Entrez le nombre de jetons", self.dimx / 2, self.dimy * (1 / 3),"purple")
            R1 = self.g.afficherTexte("Appuyer sur entrer pour valider", self.dimx / 2, self.dimy * (1 / 6),"blue")
            self.ajPoub(P7), self.ajPoub(R1)
            jetons = ''
            while True:
                touche1 = self.g.attendreTouche()
                if touche1 == "Return":
                    break
                try:
                    entier1 = int(touche1)  # Convertit la touche en entier
                    jetons += str(entier1)  # Ajouter l'entier à la chaîne de nombre
                    valeur = int(jetons)
                    self.NBP = valeur
                except ValueError:
                    er1 = self.g.afficherTexte("Veuillez entrer un entier valide.", self.dimx / 2, self.dimy / 2,"blueviolet")
                    self.ajPoub(er1)
            P6 = self.g.afficherTexte("Nombre de pieces : {}".format(self.NBP), self.dimx / 2, self.dimy * (2 / 3),"blueviolet")
            self.dijet()
            self.ajPoub(P6)
            self.g.attendreClic()
            self.vider()
            return self.mode()

    def Generation(self): #Generation des jetons graphiquement
        coords = self.dimaffichage()
        image = self.g.afficherImage(0, 0, "image_fond.jpg", self.dimx, self.dimy)
        self.g.dessinerDisque(50,330,self.rayon2,"pink"),self.g.dessinerDisque(50,390,self.rayon2,"blueviolet"),self.g.dessinerDisque(50,450,self.rayon2,"palevioletred"),self.g.dessinerDisque(50,510,self.rayon2,"darkslateblue"),self.g.dessinerDisque(50,570,self.rayon2,"royalblue")
        self.g.afficherTexte("-1",50,330),self.g.afficherTexte("-3",50,390),self.g.afficherTexte("-5",50,450),self.g.afficherTexte("-8",50,510),self.g.afficherTexte("-10",50,570)
        for coord, (val, coul) in self.dicjet.items(): #on associe les couleurs en francais avec le nom des couleurs en python
            if coul == "rose":
                couleur_disque = "pink"
            elif coul == "bleuviolet":
                couleur_disque = "blueviolet"
            elif coul == "violet pâlerouge":
                couleur_disque = "palevioletred"
            elif coul == "bleu ardoise foncé":
                couleur_disque = "darkslateblue"
            elif coul == "bleu royal":
                couleur_disque = "royalblue"
            taille = ceil(self.rayon/1.5)
            self.jeton = self.g.dessinerDisque(coord[0], coord[1], self.rayon, couleur_disque)
            self.valeur = self.g.afficherTexte(str(val), coord[0], coord[1], "black",taille)
            self.dico[self.jeton] = [coord, val, coul, self.valeur] #on creer deux dictionnaires ayant des objets graphiques en clé
            self.dicoval[self.valeur] = [coord, val, coul, self.jeton]#le premier a les disque de jeton et deuxieme la valeur ecrite

    def Grafj2(self, x):
        self.score = 0
        self.score2 = 0
        for i in range(x):
            self.poid = 0
            self.Generation()
            self.TEMPS = 1.25 * self.NBP
            debut = time.time()
            if i == 0:
                joueur_score = self.score
            else:
                joueur_score = self.score2
            score_graph = self.g.afficherTexte("Votre score est : {}".format(joueur_score), self.dimx * (1 / 3),self.dimy / 5, "plum")
            tour = self.g.afficherTexte("C'est au tour du joueur {}".format(i + 1), self.dimx * (1 / 2), self.dimy / 3,"thistle")
            lim = self.g.afficherTexte("Prix Couleur: {}".format(self.poid), self.dimx * (6 / 8), self.dimy * (1 / 5),"plum")
            max = self.g.afficherTexte("Limite : {}".format(self.limit), self.dimx * (6 / 8), self.dimy * (1 / 10),"lavenderblush")
            temps = self.g.afficherTexte("Temps disponible : {}".format(self.TEMPS), self.dimx * (2 / 8), self.dimy * (1 / 20), "lavenderblush",12)
            chronometre = self.g.afficherTexte("Temps écoulé :", self.dimx * (2 / 8), self.dimy * (1 / 10),"lavenderblush")
            cercle = set()
            while time.time() - debut < self.TEMPS:
                temps_ecoule = int(time.time() - debut)
                self.g.changerTexte(chronometre, "Temps écoulé : {} secondes".format(temps_ecoule))
                clic = self.g.attendreClic()
                x_clic, y_clic = clic.x, clic.y
                if self.g.recupererObjet(x_clic, y_clic):
                    objet_clic = self.g.recupererObjet(x_clic, y_clic)
                else:
                    objet_clic = None
                if objet_clic is not None:
                    if objet_clic in self.dico:
                        coord, val, coul, obj = self.dico[objet_clic]

                        for scorecoul, couleur in self.couleur.items():
                            if coul in couleur:
                                valcoul = scorecoul
                                break
                        if (self.poid + valcoul) > self.limit:
                            if i == 0:
                                self.score += val
                                self.g.changerTexte(score_graph, "Votre score est : {}".format(self.score))
                            else:
                                self.score2 += val
                                self.g.changerTexte(score_graph, "Votre score est : {}".format(self.score2))

                            self.poid += valcoul
                            self.g.changerTexte(lim, "Prix couleur : {}".format(self.poid))
                        else:
                            break
                        c = self.g.dessinerCercle(coord[0], coord[1], self.rayon * 1.1,"magenta")  # dessine un cercle pour montrer que le cercle est déjà cliqué
                        cercle.add(c)
                        del self.dicoval[self.dico[objet_clic][3]]
                        del self.dico[objet_clic]  # Supprimer l'objet graphique du dictionnaire

                    elif objet_clic in self.dicoval: #on fait 2 cas pour savoir si lobjet graphique cliqué est un jeton ou un texte (méthode pas tres optimal)
                        coord, val, coul, obj = self.dicoval[objet_clic]
                        for scorecoul, couleur in self.couleur.items():
                            if coul in couleur:
                                valcoul = scorecoul
                                break
                        if (self.poid + valcoul) > self.limit:
                            if i == 0:
                                self.score += val
                                self.g.changerTexte(score_graph, "Votre score est : {}".format(self.score))
                            else:
                                self.score2 += val
                                self.g.changerTexte(score_graph, "Votre score est : {}".format(self.score2))
                            self.poid += valcoul
                            self.g.changerTexte(lim, "Prix couleur : {}".format(self.poid))
                        else:
                            break
                        c = self.g.dessinerCercle(coord[0], coord[1], self.rayon * 1.1,"magenta")  # dessine un cercle pour montrer que le cercle est déjà cliqué
                        cercle.add(c)
                        del self.dicoval[objet_clic]
                        del self.dico[obj]  # Supprimer l'objet graphique du dictionnaire
            for x in cercle:
                self.g.supprimer(x)
            self.g.supprimer(tour), self.g.supprimer(score_graph), self.g.supprimer(lim), self.g.supprimer(
                max), self.g.supprimer(chronometre), self.g.supprimer(temps)
        poubtemp = [] #on creer une poubelle pour supprimer les objets graphiques qui vont apparaitre ci dessous
        self.g.dessinerRectangle(0, 0, self.dimx+1, self.dimy+1, "black") #on dessine un carré noir car nous avons pas reussi a utiliser la  fonction tout supprimer sur la nouvelle version de tkiteasy
        image = self.g.afficherImage(0, 0, "image_fin.jpg", self.dimx, self.dimy)
        R5 = self.g.afficherTexte("Le score du joueur 1 est : {}".format(self.score), self.dimx * (1 / 2), self.dimy / 3, "lavender")
        poubtemp.append(R5)
        if self.score2 != 0:
            R1 = self.g.afficherTexte("Le score du joueur 2 est : {}".format(self.score2), self.dimx * (1 / 2),self.dimy / 2, "lavender")
            poubtemp.append(R1)
            if self.score > self.score2:
                R2 = self.g.afficherTexte("Le gagnant est le Joueur 1", self.dimx / 2, self.dimy * 3 / 4, "violet")
                poubtemp.append(R2)
            elif self.score < self.score2:
                R3 = self.g.afficherTexte("Le gagnant est le Joueur 2", self.dimx / 2, self.dimy * 3 / 4, "violet")
                poubtemp.append(R3)
            else:
                R4 = self.g.afficherTexte("Il y a égalité", self.dimx / 2, self.dimy * 3 / 4, "violet")
                poubtemp.append(R4)
        menu = self.g.afficherTexte("Retour au menu principal", self.dimx * (1 / 2), self.dimy * 5 / 6, "darkorchid")
        poubtemp.append(menu)
        while True:
            clic = self.g.attendreClic()
            if self.g.recupererObjet(clic.x, clic.y) == menu:
                for x in poubtemp:
                    self.g.supprimer(x)
                return self.menujeu()

    def naif(self):
        self.poid=0
        self.score=0
        self.Generation()
        self.g.attendreClic()
        combinaisons = []
        # Calculer les ratios et les stocker avec les informations nécessaires
        ratios = []
        for coord, (val, coul) in self.dicjet.items():
            for scorecoul, couleur in self.couleur.items():
                if coul in couleur:
                    prix_couleur = scorecoul
                    break  # Prix de la couleur de la pièce
            ratio = val / abs(prix_couleur)
            ratios.append((coord, val, prix_couleur, ratio))

        # Trier les ratios par ordre décroissant
        ratios.sort(key=lambda x: x[3], reverse=True)
        print(ratios)
        # Parcourir les ratios triés et sélectionner les meilleures combinaisons
        for coord, val, prix_couleur, ratio in ratios: #on prend les valeurs dans lordre de sortie (donc ratio decroissant meme si normalement les valeurs ne sorte pasforcement dans lordre ca semble marcher avec cette version de python)
            #prix_couleurpos = abs(prix_couleur)  # Prix de la couleur de la pièce
            if (self.poid + prix_couleur) >= self.limit:
                combinaisons.append((coord, val, coul))
                self.poid += prix_couleur
                self.score += val

        # Afficher les combinaisons
        for coord, val, coul in combinaisons:
            a = self.g.dessinerCercle(coord[0], coord[1], self.rayon * 1.1, "magenta")
        T1 = self.g.afficherTexte("Le prix total est {}".format(self.poid), self.dimx / 2, self.dimy * (1 / 3),"slateblue")
        T2 = self.g.afficherTexte("La valeur total est {}".format(self.score), self.dimx / 2, self.dimy * (2 / 5),"slateblue")
        menu = self.g.afficherTexte("Retour Menu", self.dimx * 0.5, self.dimy * (1 / 5), "mediumorchid")
        self.ajPoub(menu), self.ajPoub(T1), self.ajPoub(T2)
        clic = self.g.attendreClic()
        if self.g.recupererObjet(clic.x, clic.y) == menu:
            self.g.supprimer(T1), self.g.supprimer(T2), self.g.supprimer(menu)
            self.g.dessinerRectangle(0, 0, self.dimx + 1, self.dimy + 1, "black")
            return self.menujeu()

    def resIntelligente(self):
        self.Generation()  # Générer les pièces
        menu = self.g.afficherTexte("Retour Menu", self.dimx * 0.5, self.dimy * (1 / 5), "mediumorchid")
        valeurs = []  # Liste des valeurs des pièces
        poids = []  # Liste des prix de couleur des pièces
        selection = []  # Liste des pièces sélectionnées
        # Préparer les valeurs et les poids des pièces
        for coord, (val, coul) in self.dicjet.items():
            valeurs.append(val)
            for scorecoul, couleur in self.couleur.items():
                if coul in couleur:
                    prix_couleur = scorecoul
                    break
            poids.append(abs(prix_couleur))
        # On applique l'algo qui qui selectionne les meilleurs pieces
        limit = abs(self.limit)  # La capacité est égale à la limite
        resultat, selection, prix = self.sélection_objets(valeurs, poids, limit)
        # Dessiner les pièces sélectionnées
        for i in selection:
            for coords, (vals, couls) in self.dicjet.items():
                for scorecoul, couleur in self.couleur.items():
                    if couls in couleur:
                        poids = - scorecoul
                        break
                if (vals, poids) == i:
                    a = self.g.dessinerCercle(coords[0], coords[1], self.rayon * 1.1, "magenta")
                    self.g.attendreClic()
        T1 = self.g.afficherTexte("La valeur total est {}".format(resultat), self.dimx / 2, self.dimy * (2 / 5),"slateblue")
        T2 = self.g.afficherTexte("Le prix total est {}".format(prix), self.dimx / 2, self.dimy * (1 / 3),"slateblue")
        while True:
            clic = self.g.attendreClic()
            if self.g.recupererObjet(clic.x,clic.y) == menu:
                self.g.supprimer(menu),self.g.supprimer(T1), self.g.supprimer(T2)
                self.menujeu()

    def sélection_objets(self, valeurs, poids, limite): #algo qui selectionne les meileurs jetons et renvoie leur score total
        n = len(valeurs)
        lp = [[0] * (limite + 1) for _ in range(n + 1)]  # dp est le tableau pour enregistrer le plus gros score en fonction de la limite

        for i in range(1, n + 1):
            for w in range(1, limite + 1):  # on regarde si le poids actuel est supérieur à la limite, si il ne l'est pas on prend celui d'avant
                if poids[i - 1] > w:
                    lp[i][w] = lp[i - 1][w]
                else:  # on regarde le max entre prendre ou ne pas prendre le jeton
                    lp[i][w] = max(lp[i - 1][w], lp[i - 1][w - poids[i - 1]] + valeurs[i - 1])
        print(lp)
        resultat = lp[n][limite]
        print(resultat)
        sélection = []
        w = limite
        for i in range(n, 0, -1):  # La boucle parcourt les objets de la liste en commençant par le dernier et en allant vers le premier
            if resultat <= 0: # On verifie a chaque fois si le résultat est inférieur ou égal à zéro.
                break # Si oui, cela signifie que nous avons atteint le meilleur score possible ou que la limite de poids a été dépassée
            if resultat == lp[i - 1][w]: # Si le résultat est égal à ca, cela signifie que l'objet actuel n'a pas été pris
                continue
            else:
                sélection.append((valeurs[i - 1], poids[i - 1])) #Sinon, cela signifie que l'objet a contribué au meilleur score
                resultat -= valeurs[i - 1] # ON met à jour le résultat et la limite
                w -= poids[i - 1]
        limite_atteinte = limite - w
        return lp[n][limite], sélection, limite_atteinte

    def ajPoub(self, obj): #Finalement peu utilisé car ces fonctions semblaient poser probleme par moment
        self.poubelle.append(obj)
    def vider(self):
        for x in self.poubelle:
            self.g.supprimer(x)
        del self.poubelle[:]

jeu = Projet()