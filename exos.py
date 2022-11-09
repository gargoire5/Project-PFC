DEBUT
# ECRIRE "Bonjour Monde"


assertionUn = (( (365 * 3) / (24-(16-8)) ) * (rh) > r ) == (e * s < r)

(( (365 * 3) / (24-(16-8)) ) * (rh) > r ) True or False ?
(16-8= 8)
(24-8 = 16)
(365 * 3 ) = 1095
(1095/16) = 68.4375
(68.4375 * 230) = 15740.625
15740.625 > 12000 True

(e * s < r) True or False ?
(10*1250) = 12500
12500 < 12000 False 

# assertionUn = assertUnPtUn = assertUnPtDeux # False
r = 12000
s = 1250
e = 10
rh = 230


assertionDeux = ((365 * 3) / (4 - (12 - 8)) * (rh) > r) == (e * s < r)

(( (365 * 3) / (4-(12-8)) ) * (rh) > r ) True or False ?
(12-8= 4)
(4-4 = 0)
(365 * 3 ) = 1095
(1095/0) = error false 
(68.4375 * 230) = 15740.625
15740.625 > 12000 False

(e * s < r) True or False ?
(10*1250) = 12500
12500 < 12000 False 


# assertionUn = assertUnPtUn = assertUnPtDeux # True


def retournerSixPlusTrois():
    return 6 + 3
def retournerSixPlusX(){
    return 6 + 3
}
print("Qui vole un " + retournerSixPlusTrois() "vole un boeuf.")


-add (x,y)
def add(x,y):
    return x + y

-sub (x,y)
def sub(x,y):
    return x - y

-multiply (x,y)
def multiply(x,y):
    return x * y

-divide (x,y)
def divide(x,y):
    if y == 0:
        return "error"
    else :
        return x / y

-modulo (x,y)
def modulo(x,y):
    if y == 0:
        return "error"
    else :
        return x % y

-Calcule de salaire que je peux gagner par seconde:
Salaire horaire;
Heure par jour ouvrable;
Nb jour ouvrabe;
def CalculeSalaireSeconde(SalaireHoraire, HeureOuvrable, NbJourOuvrable):
    # Assigner a Salaire Annuel, le nombre d'heure travaillées pae an
    salaireAnnuel = SalaireHoraire * HeureOuvrable * NbJourOuvrable
    # Calculer, puis asssigner a nombre de seconde par an, le nombre de seconde dans une année non-bisextile
    nombreDeSecondeParAn = 60 * 60 * 24 * 365
    # Retouner le salaire Annuel divisé par le nombre de seconde par an
    return salaireAnnuel / nombreDeSecondeParAn

-Calcule salaire net:
Salaire Brut;
Coeff;
def withdrawFees(total, percent):
    #Calcule du montant des taxes a retirer :
    fees = total * (percent / 100)
    #Retourner la valeur totale moins les taxes
    return totale - fees 

def calculeSalaireNet(salaireBrut, coeff):
    #Calculer et retourner le Salaire Net a partir du salaire brut
    return withdrawFees(salaireBrut, coeff)

def calculeSalaireNet(salaireBrut, public):
    # Si j'occupe un poste de la fonction public
    if public : 
        # alors je retourne le salaire brut - 15% de taxes
        return withdrawFees(salaireBrut, 15)
    # Sinon ? C'est ce je suis tavailleur dans le secteur privé, alors je retourne le salaire brut - 23% de douille à l'ancienne
    else:
        return withdrawFees(salaireBrut, 23)

def divide(x,y):
    # si Y est egal a 0, alors la division est impossible
    if y == 0:
    # Alors renvoyer un message d'erreur
        print("Bah alors")
        return None 
    # Sinon
    else :
    # Retouner le calcul x / y
        return x / y


def input():
# Renvoie un caractere de type string au hasard


# Exercice :
    # Faire un mini jeu qui affiche un message lorsque input revoie le bon caractere 
    # Le caractere doit etre parametrable 



def miniJeuCaractere(x):
    #tant que la lettre de input est pas la lettre choisie 
    while input ==! x :
    # retourne input quand x est egal a input
    print("Vous avez gagné")
    return input

correction:
def miniGame(lettre):
    #Je defini une variable caractereAléatoire qui permet de contenir le caratere généré avec input
    caractereAléatoire = input()
    #Tant que caractereAléatoire est different de la lettre souhaitee
    while caractereAléatoire != lettre:
        #Alors j'attribue a caractereAléatoire, une nouvelle lettre
        caractereAléatoire = input() 
    #Si la lettre souhaitee est egale au caractereAléatoire,
    if caractereAléatoire == lettre:
        #Alors j'affiche un message de victoire
        print("Vous avez gagné")

miniGame('A')
    



tableau = [3,5,5,6,66,99,22,74,36,25,96,58,25,15,48]

#Pour recuperer 15 je prend dans tableau l'index 14

print(tableau[14]) #Afficher 15

len(tableau) #Renvoie la longueur du tableau

prenom = "Grégoire"
nom = "Portevin"
identite = nom + prenom # retourne "GrégoirePortevin"
identite = nom + ' ' + prenom # retourne "Grégoire Portevin"
*
integerValue = 342 # renvoie 342
stringIntegerValue = str(342) # renvoie "342"

# Exercice 1
# Faire une fonction qui concatene 2 chaines de caractere, les séparents par une virgule 

def fonction(chaineDeCaractereUn, chaineDeCaractereDeux):
    # Je concatene les 2 chaines de carctere en les séparant par une virgule et retourne "Je saute, je mange"
    chaineDeCaractere = chaineDeCaractereUn + ", " + chaineDeCaractereDeux
    # Definir que la fonction est egale a chaine de caractere
    fonction == chaineDeCaractere
    #Ecrire la chaine de caractere
    print(chaineDeCaractere)
# Appeler la fonction
fonction("Je mange", "je saute")


# Exercice 2
# Faire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere 
# avec l'ensembles des ocurrences d'un chiffre e.g.:
# Pour tableau = [0,1,1,1,0,1,1,0,1]
# la fonction(tableau, 0) doit renvoyer "0, 4, 7" n'hesiter pas a implementer la premiere fonction








































FIN