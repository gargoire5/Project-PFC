grid=[[" "," "," "],[" "," "," "],[" "," "," "]]

lignechoisie=2
colonnechoisie=1



def displayGrid():
    print (grid[0])
    print (grid[1])
    print (grid[2])

def CheckWin(quelJoueur, gagnant, conditionWin):
    if (grid[0][0]==grid[0][1] and grid[0][0]==grid[0][2] and grid[0][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True       
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[0][0]==grid[1][0] and grid[0][0]==grid[2][0] and grid[0][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[0][0]==grid[1][1] and grid[0][0]==grid[2][2] and grid[0][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True
    if (grid[2][0]==grid[1][1] and grid[2][0]==grid[0][2] and grid[2][0]!=" "):
        if quelJoueur==2:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
        if quelJoueur==1:
            print("Le joueur 1 a gagné!!!")
            conditionWin = True

    return conditionWin

def theGame(conditionWin):
    displayGrid()
    print(grid[0][0])
    print(grid[0][1])
    print(grid[0][2])
    Win=0
    quelJoueur=1
    nbTour=0
    conditionWin = False
    print ("Bienvenue dans le jeux du Morpion vous pourrez jouer les croix X ")
    print ("Pour chaque tours vous rentrerez le numero de la colonne que vous voulez remplir puis le numero de la ligne")
    while conditionWin!=True:
        if nbTour==9:
            print("Egalité")
            break
        if quelJoueur==1:
            print("Joueur ",quelJoueur, "jouez")
            nbTour=nbTour + 1
            colonne=input("Entrez le numero de la colonne : ")
            ligne=input("Entrez le numero de la ligne : ")
            print("Vous avez joué la case ("+colonne+","+ligne+")") 
            while grid[int(ligne)][int(colonne)]!=" ":
                print("Cette case est deja jouée ! Saisissez une autre case svp !")
                colonne=input("Entrez le numero de la colonne : ")
                ligne=input("Entrez le numero de la ligne : ")
                print("Vous avez joué la case ("+colonne+","+ligne+")")
            grid[int(ligne)][int(colonne)]="X"
            if (CheckWin(quelJoueur, Win, conditionWin) == True):
               break;
            quelJoueur=quelJoueur+1
            
        
        displayGrid()
        if quelJoueur==2:
            print("Joueur ",quelJoueur, "jouez")
            nbTour=nbTour + 1
            colonne=input("Entrez le numero de la colonne : ")
            ligne=input("Entrez le numero de la ligne : ")
            print("Vous avez joué la case ("+colonne+","+ligne+")") 
            while grid[int(ligne)][int(colonne)]!=" ":
                print("Cette case est deja jouée ! Saisissez une autre case svp !")
                colonne=input("Entrez le numero de la colonne : ")
                ligne=input("Entrez le numero de la ligne : ")
                print("Vous avez joué la case ("+colonne+","+ligne+")")
            grid[int(ligne)][int(colonne)]="O"
            if (CheckWin(quelJoueur, Win, conditionWin) == True):
                break;
            quelJoueur=quelJoueur-1  
        displayGrid()
            
        
        
theGame(False)