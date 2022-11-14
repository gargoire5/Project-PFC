from random import randint

liste = ["pierre", "feuille", "ciseau"]


def roundNombreParMatch(nombreDeRound):
    print("Combien de manche souhaitez vous jouer ? : Taper le nombre de manches que vous souhaiter jouer")
    nombreDeRound = int(input())
    return print("Vous allez jouer " + str(nombreDeRound)+ " round")


def jeuPierreFeuilleCiseauxEntreJoueur():
    roundJoue = 0
    nombreDePointJoueurUn = 0
    nombreDePointJoueurDeux = 0
    roundNombreParMatch([])
    while roundJoue != :
        print("C'est parti entrer soit pierre, soit feuille, soit ciseau")
        choixJoueurUn = input()
        choixJoueurDeux = input()

        if choixJoueurUn == "pierre" and choixJoueurDeux == "pierre":
            print("Vous avez fait égalité")
        elif choixJoueurUn == "ciseau" and choixJoueurDeux == "ciseau":
            print("Vous avez fait égalité") 
        elif choixJoueurUn == "feuille" and choixJoueurDeux == "feuille":
            print("Vous avez fait égalité")
        elif choixJoueurUn == "pierre" and choixJoueurDeux == "ciseau":
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1
        elif choixJoueurUn == "ciseau" and choixJoueurDeux == "feuille":
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1
        elif choixJoueurUn == "feuille" and choixJoueurDeux == "pierre":
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1
        elif choixJoueurDeux == "pierre" and choixJoueurUn == "ciseau":
            print("Joueur 2 a gagné")
            nombreDePointJoueurDeux += 1
        elif choixJoueurDeux == "ciseau" and choixJoueurUn == "feuille":
            print("Joueur 2 a gagné")
            nombreDePointJoueurDeux += 1
        elif choixJoueurDeux == "feuille" and choixJoueurUn == "pierre":
            print("Joueur 2 a gagné")
            nombreDePointJoueurUn += 1
        else:
            choixJoueurDeux == " " or choixJoueurUn == " "
            print("Veuillez rentrer une valeur")

        roundJoue += 1

    if nombreDePointJoueurUn > nombreDePointJoueurDeux:
        print("Victoire du Joueur 1, Felicitation")
    elif nombreDePointJoueurUn < nombreDePointJoueurDeux:
        print("Victoire du Joueur 2, Felicitation")
    else:
        nombreDePointJoueurUn == nombreDePointJoueurDeux
        print("C'est une égalité incroyable !!!")

def jeuPierreFeuilleCiseauxJoueurOrdi():
    roundJoue = 0
    nombreDePointJoueurUn = 0
    nombreDePointOrdi = 0
    roundNombreParMatch([])
    while roundJoue != roundNombreParMatch:
        print("C'est parti entrer soit pierre, soit feuille, soit ciseau")
        choixJoueurUn = input(liste)
        choixOrdi = randint(liste) 
        if choixJoueurUn == " ":
            return "Il y a une erreur"
        if choixJoueurUn == " ":
            return "Il y a une erreur"

        if choixJoueurUn == "pierre" and choixOrdi == "pierre":
            print("Vous avez fait égalité")
        elif choixJoueurUn == "ciseau" and choixOrdi == "ciseau":
            print("Vous avez fait égalité")
        else: 
            choixJoueurUn == "feuille" and choixOrdi == "feuille"
            print("Vous avez fait égalité")
        
        if choixJoueurUn == "pierre" and choixOrdi == "ciseau":
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1
        elif choixJoueurUn == "ciseau" and choixOrdi== "feuille":
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1
        else: 
            choixJoueurUn == "feuille" and choixOrdi == "pierre"
            print("Joueur 1 a gagné")
            nombreDePointJoueurUn += 1

        if choixOrdi == "pierre" and choixJoueurUn == "ciseau":
            print("Joueur 2 a gagné")
            nombreDePointJoueurDeux += 1
        elif choixOrdi == "ciseau" and choixJoueurUn == "feuille":
            print("Joueur 2 a gagné")
            nombreDePointJoueurDeux += 1
        else: 
            choixOrdi == "feuille" and choixJoueurUn == "pierre"
            print("Joueur 2 a gagné")
            nombreDePointJoueurUn += 1

        roundJoue = roundJoue + 1

    if nombreDePointJoueurUn > nombreDePointOrdi:
        print("Victoire du Joueur 1, Felicitation")
    elif nombreDePointJoueurUn < nombreDePointOrdi:
        print("Victoire du Joueur 2, Felicitation")
    else:
        nombreDePointJoueurUn == nombreDePointOrdi
        print("C'est une égalité incroyable !!!")
        
def choixModeDeJeu(quelChoix):
    print("Vous allez jouer au chifoumi : taper 1 si vous voulez jouer avec un joueur ou taper 2 si vous voulez jouer avec un Bot")
    quelChoix = int(input())
    if quelChoix == 1:
        print("Vous allez jouer contre un autre joueur")
        jeuPierreFeuilleCiseauxEntreJoueur()
    elif quelChoix == 2:
        print("Vous allez jouer contre un BOT")
        jeuPierreFeuilleCiseauxJoueurOrdi()
    else:
        return print("Veuilez mettre une valeur correct, pour choisir un mode de jeu")
choixModeDeJeu([])




        
        
        

