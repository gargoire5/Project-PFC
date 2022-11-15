from random import randint

liste2 = [0,1,2,3,4,5]
liste = ["pierre", "feuille", "ciseau"]

print("Bienvenue dans le jeu du chifoumi, le jeu ce passe face a une IA. Vous pouvez choisir le nombre de Manches jusqu'à 5 ")

def jeuPierreFeuilleCiseauxJoueurOrdi():
    print("Combien de manche souhaitez vous jouer ? : Taper le nombre de manches que vous souhaiter jouer")
    nombreDeRound = liste2[int(input())]
    roundJoue = 0
    nombreDePointJoueur = 0
    nombreDePointOrdi = 0
    while roundJoue != nombreDeRound:
        print("C'est parti entrer soit pierre, soit feuille, soit ciseau")
        choixJoueurUn = input()
        choixOrdi = liste[randint(0,2)]
        if choixJoueurUn == liste[0] and choixOrdi == liste[0]:
            print("Vous avez fait égalité")
        elif choixJoueurUn == liste[1] and choixOrdi == liste[1]:
            print("Vous avez fait égalité")
        elif choixJoueurUn == liste[2] and choixOrdi == liste[2]:
            print("Vous avez fait égalité")
        elif choixJoueurUn == liste[0] and choixOrdi == liste[2]:
            print("Joueur 1 a gagné")
            nombreDePointJoueur += 1
        elif choixJoueurUn == liste[2] and choixOrdi == liste[1]:
            print("Joueur 1 a gagné")
            nombreDePointJoueur += 1
        elif choixJoueurUn == liste[1] and choixOrdi == liste[0]:
            print("Joueur 1 a gagné")
            nombreDePointJoueur += 1
        elif choixOrdi == liste[0] and choixJoueurUn == liste[2]:
            print("L'IA a gagné")
            nombreDePointOrdi += 1
        elif choixOrdi == liste[2] and choixJoueurUn == liste[1]:
            nombreDePointOrdi += 1
        else:
            choixOrdi == liste[1] and choixJoueurUn == liste[0]
            print("L'IA a gagné")
            nombreDePointOrdi += 1

        roundJoue = roundJoue + 1

    if nombreDePointJoueur > nombreDePointOrdi:
        print("Victoire du Joueur 1, Felicitation")
    elif nombreDePointJoueur < nombreDePointOrdi:
        print("Victoire de l'IA, Felicitation")
    else:
        nombreDePointJoueur == nombreDePointOrdi
        print("C'est une égalité incroyable !!!") 

    print("******Point******")
    print("Joueur :", nombreDePointJoueur) 
    print("Ordi :", nombreDePointOrdi)

    return roundJoue
jeuPierreFeuilleCiseauxJoueurOrdi()


        
        
        

