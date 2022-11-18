#initialiser un tableau appeler grid contenant trois tableaus dans lesquels on retrouve dans chauqune une valeur sous forme str contenant un espace

#definir la fonction dislaygrid qui ne prend rien en paramettre
    #afficher le premier tableau du tableau contenant tout les tableau
    #afficher le deuxieme tableau du tableau contenant tout les tableau
    #afficher le troisieme tableau du tableau contenant tout les tableau

#definir la fonction the game qui ne prend rien en parametre
    #initialiser la variable win a 0
    #initialiser la variable quelJoueur a 1
    #écrire Bienvenue dans le jeux du Morpion vous pourrez jouer les croix X 
    #écrire Pour chaque tours vous rentrerez le numero de la colonne que vous voulez remplir puis le numero de la ligne
    #tant que win n'est pas egal a 1
        #si la variable quelJoueur est égal a 1
            #alors mettre a colonne la valeur de la fonction input entrez le numero de votre colonne : 
            #alors mettre a ligne la valeur de la fonction input entrez le numero de votre ligne : 
            #ecrire vous avez jouer la case colonne , ligne 
            #tant que dans grid les coordonné du premier tableau a la valeur ligne et du tableau  a la valeur ligne et qui a l'interieur est a la valeur colonne n'est pas egal a un espace sous forme strqui correspond
                #ecrire "cette case est deja jouée ! saisissez une autres case svp !"
                #alors mettre a colonne la valeur de la fonction input entrez le numero de votre colonne : 
                #alors mettre a ligne la valeur de la fonction input entrez le numero de votre ligne : 
                #ecrire "vous avez joué la case "+colonne+,+ligne+""
            #mettre la valeur du tableau gris qui correspond aux tableau ligne et dont la valeur du ce meme tableau a la coodonné est colonne a x
            #mettre la variable quelJoueur a la valeur quelJoueur + 1
        #appeler la fonction displayGrid
        #si la variable quelJoueur est égal a 2
            #alors mettre a colonne la valeur de la fonction input entrez le numero de votre colonne : 
            #alors mettre a ligne la valeur de la fonction input entrez le numero de votre ligne : 
            #ecrire vous avez jouer la case colonne , ligne 
            #tant que dans grid les coordonné du premier tableau a la valeur ligne et du tableau  a la valeur ligne et qui a l'interieur est a la valeur colonne n'est pas egal a un espace sous forme strqui correspond
                #ecrire "cette case est deja jouée ! saisissez une autres case svp !"
                #alors mettre a colonne la valeur de la fonction input entrez le numero de votre colonne : 
                #alors mettre a ligne la valeur de la fonction input entrez le numero de votre ligne : 
                #ecrire "vous avez joué la case "+colonne+,+ligne+""
            #mettre la valeur du tableau gris qui correspond aux tableau ligne et dont la valeur du ce meme tableau a la coodonné est colonne a x
            #mettre la variable quelJoueur a la valeur quelJoueur - 1
        #appeler la fonction displayGrid
        #si la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 0 et 1 du tableau grid et que la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 0 et 2 et que la valeur aux coordoné 0 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 1 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 1 du tableau grid et que la valeur aux coordoné 1 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 2 et que la valeur aux coordoné 1 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 1 du tableau grid et que la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 2 et que la valeur aux coordoné 2 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 0 du tableau grid et que la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 0 et que la valeur aux coordoné 0 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 1 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 1 du tableau grid et que la valeur aux coordoné 1 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 2 et que la valeur aux coordoné 1 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 1 du tableau grid et que la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 2 et que la valeur aux coordoné 2 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 1 du tableau grid et que la valeur aux coordoné 0 et 0 du tableau grid est egal a la valeur aux coordonée 2 et 2 et que la valeur aux coordoné 0 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 1 et 1 du tableau grid et que la valeur aux coordoné 2 et 0 du tableau grid est egal a la valeur aux coordonée 0 et 2 et que la valeur aux coordoné 2 et 0 du tableau grid n'est pas egal a u espace sous forme str 
            #alors mettre la variable win a la valeur win + 1
        #si la variable win  est egal a 1
            #alors si la variable quelJoueur est egal a 2:
                #alors ecrire "le joueur 2 a gagné!!!"
            #si la variable quelJoueur est egal a 1:
                #alors ecrire "le joueur 1  a gagné!!! "
            #sinon
                #ecire "egalité!!!"