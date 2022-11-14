# Debut

# Appeler la fonction input qui renvoie un caractere de type string au hasard
# Appeler la fonction random qui renvoie a un nombre aleatoire qui renvoi a un nombre entier entre 1 et 3
# Créer une liste avec comme index "pierre", "feuille", "ciseau"

# Definir une fonction choixModeDeJeu qui prend commme parametre la valeur quelChoix
    # Ecrire "Vous allez jouer au chifoumi : taper 1 si vous voulez jouer avec un joueur ou taper 2 si vous voulez jouer avec un Bot"
    # Si la valeur de input est egal a 1
        # Alors lancer la fonction jeuPierreFeuilleCiseauxEntreJoueur
    # Sinon si la valeur de input est egal a 2
        # Alors lancer la fonction jeuPierreFeuilleCiseauxJoueurOrdi
    # Sinon retourner "Veuilez mettre une valeur correct, pour choisir un mode de jeu"

# Definir la fonction roundNombreParMatch qui en parametre nombreDeRound
    # Ecrire "Combien de manche souhaitez vous jouer ? : Taper le nombre de manches que vous souhaiter jouer"
    # Assigner a nombreRound la valeur de la fonction input3
    # Retourner nombreRound

# Definir la fonction jeuPierreFeuilleCiseauxEntreJoueur avec comme parametre la valeur x
    # Initialiser la variable roundJoue a la valeur 0
    # Initialiser la variable nombreDePointJoueurUn a la valeur 0
    # Initialiser la variable nombreDePointJoueurDeux a la valeur 0
    # Lancer la fonction roundNomnreParMatch
    # Tant que roundJouePendantLeMatch n'est pas egal a roundNombreParMatch
        # Ecrire "C'est parti entrer soit pierre, soit feuille, soit ciseau"
        # Assigner a choixJoueurUn la valeur de la fonction input1 avec comme valeur la liste créer
        # Assigner a choixJoueurDeux la valeur de la fonction input2 avec comme valeur la liste créer
        # Si choixJoueurUn est egale a " "
            # Alors retourer "Il y a une erreur"
        # Si choixJoueurDeux est egale a " "
            # Alors retourer "Il y a une erreur"


        # Si choixJoueurUn est egale a "pierre" et que choixJoueurDeux est egale a "pierre"
            # Alors ecrire "Vous avez fait égalité" 
        # Sinon si choixJoueurUn est egale a "feuille" et que choixJoueurDeux est egale a "feuille"
            # Alors ecrire "Vous avez fait égalité" 
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixJoueurDeux est egale a "ciseau"
            # Alors ecrire "Vous avez fait égalité" 

        # Si choixJoueurUn est egale a "pierre" et que choixJoueurDeux est egale a "ciseau"
            # Alors ecrire "Joueur 1 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        # Sinon si choixJoueurUn est egale a "feuille" et que choixJoueurDeux est egale a "pierre"
            # Alors ecrire "Joueur 1 a gagné" 
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixJoueurDeux est egale a "feuille"
            # Alors ecrire "joueur 1 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        

        # Si choixJoueurUn est egale a "feuille" et que choixJoueurDeux est egale a "ciseau"
            # Alors ecrire "joueur 2 a gagner" 
            # Alors ajouter 1 a la variable nombreDePointJoueurDeux
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixJoueurDeux est egale a "pierre"
            # Alors ecrire "joueur 2 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurDeux 
        # Sinon si choixJoueurUn est egale a "pierre" et que choixJoueurDeux est egale a "feuille"
            # Alors ecrire "Joueur 2 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurDeux
    
        # Assigner a roundJoue la valeur de rounJoue + 1

    # Si nombreDePointJoueurUn est superieur a nombreDePointJoueurDeux
        # Alors ecrire "Victoire du Joueur 1, Felicitation"
    # Si nombreDePointJoueurDeux est superieur a nombreDePointJoueurUn
        # Alors ecrire "Victoire du joueur 2, Felicitation"
    # Si nombreDePointJoueurUn est egal a nombreDePointJoueurDeux
        # Alors ecrire "C'est une égalité incroyable !!!"

# Definir la fonction jeuPierreFeuilleCiseauxJoueurOrdi avec comme parametre la valeur x
    # Initialiser la variable roundJoue a la valeur 0
    # Initialiser la variable nombreDePointJoueurUn a la valeur 0
    # Initialiser la variable nombreDePointOrdi a la valeur 0
    # Lancer la fonction roundNomnreParMatch
    # Tant que roundJouePendantLeMatch n'est pas egal a roundNombreParMatch
        # Ecrire "C'est parti entrer soit pierre, soit feuille, soit ciseau"
        # Assigner a choixJoueurUn la valeur de la fonction input1 avec comme valeur la liste créer
        # Assigner a choixOrdi la valeur de la fonction random avec comme valeur la liste créer
        # Si choixJoueurUn est egale a " "
            # Alors retourer "Il y a une erreur"
        # Si choixOrdi est egale a " "
            # Alors retourer "Il y a une erreur"

        # Si choixJoueurUn est egale a "pierre" et que choixOrdi est egale a "pierre"
            # Alors ecrire "Vous avez fait égalité" 
        # Sinon si choixJoueurUn est egale a "feuille" et que choixOrdi est egale a "feuille"
            # Alors ecrire "Vous avez fait égalité" 
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixOrdi est egale a "ciseau"
            # Alors ecrire "Vous avez fait égalité" 

        # Si choixJoueurUn est egale a "pierre" et que choixOrdi est egale a "ciseau"
            # Alors ecrire "Joueur 1 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        # Sinon si choixJoueurUn est egale a "feuille" et que choixOrdi est egale a "pierre"
            # Alors ecrire "Joueur 1 a gagné" 
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixOrdi est egale a "feuille"
            # Alors ecrire "joueur 1 a gagné"
            # Alors ajouter 1 a la variable nombreDePointJoueurUn 
        

        # Si choixJoueurUn est egale a "feuille" et que choixOrdi est egale a "ciseau"
            # Alors ecrire "joueur 2 a gagner" 
            # Alors ajouter 1 a la variable nombreDePointOrdi
        # Sinon si choixJoueurUn est egale a "ciseau" et que choixOrdi est egale a "pierre"
            # Alors ecrire "joueur 2 a gagné"
            # Alors ajouter 1 a la variable nombreDePointOrdi
        # Sinon si choixJoueurUn est egale a "pierre" et que choixOrdi est egale a "feuille"
            # Alors ecrire "Joueur 2 a gagné"
            # Alors ajouter 1 a la variable nombreDePointOrdi
    
        # Assigner a roundJoue la valeur de rounJoue + 1

    # Si nombreDePointJoueurUn est superieur a nombreDePointOrdi
        # Alors ecrire "Victoire du Joueur 1, Felicitation"
    # Si nombreDePointOrdi est superieur a nombreDePointJoueurUn
        # Alors ecrire "Victoire de l'ordinateur, Felicitation"
    # Si nombreDePointJoueurUn est egal a nombreDePointOrdi
        # Alors ecrire "C'est une égalité incroyable !!!"

# Fin
