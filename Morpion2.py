grid=[["","",""],["","",""],["","",""]]

lignechoisie=2
colonnechoisie=1



def displayGrid():
    print (grid[0])
    print (grid[1])
    print (grid[2])

def CheckWin(Joueur, gagnant, conditionWin):
    if (grid[0][0]==grid[0][1] and grid[0][0]==grid[0][2] and grid[0][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                conditionWin = True
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                    conditionWin = True
                else:
                    print("égalité!!!")
                    conditionWin = True
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                conditionWin = True
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")       
                else:
                    print("égalité!!!")
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                else:
                    print("égalité!!!")
    if (grid[0][0]==grid[1][0] and grid[0][0]==grid[2][0] and grid[0][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                else:
                    print("égalité!!!")
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                else:
                    print("égalité!!!")
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                else:
                    print("égalité!!!")
    if (grid[0][0]==grid[1][1] and grid[0][0]==grid[2][2] and grid[0][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
                if Joueur==1:
                    print("Le joueur 1 a gagné!!!")
                else:
                    print("égalité!!!")
    if (grid[2][0]==grid[1][1] and grid[2][0]==grid[0][2] and grid[2][0]!=" "):
        gagnant=gagnant+1
        if gagnant==1:
            if Joueur==2:
                print("Le joueur 2 a gagné!!!")
            if Joueur==1:
                print("Le joueur 1 a gagné!!!")
            else:
                print("égalité!!!")
    return conditionWin

def theGame():
    displayGrid()
    print(grid[0][0])
    print(grid[0][1])
    print(grid[0][2])
    Win=0
    condition = False
    quelJoueur=1
    print ("Bienvenue dans le jeux du Morpion vous pourrez jouer les croix X ")
    print ("Pour chaque tours vous rentrerez le numero de la colonne que vous voulez remplir puis le numero de la ligne")
    while condition!=True:
        if quelJoueur==1:
            print("Joueur ",quelJoueur, "jouez")
            CheckWin(quelJoueur, Win, condition)
            colonne=input("Entrez le numero de la colonne : ")
            ligne=input("Entrez le numero de la ligne : ")
            print("Vous avez joué la case ("+colonne+","+ligne+")") 
            while grid[int(ligne)][int(colonne)]!="":
                print("Cette case est deja jouée ! Saisissez une autre case svp !")
                colonne=input("Entrez le numero de la colonne : ")
                ligne=input("Entrez le numero de la ligne : ")
                print("Vous avez joué la case ("+colonne+","+ligne+")")
            grid[int(ligne)][int(colonne)]="X"
            quelJoueur=quelJoueur+1
            print("Joueur ",quelJoueur, "jouez")
        
        displayGrid()
        if quelJoueur==2:
            print("Joueur ",quelJoueur, "jouez")
            CheckWin(quelJoueur, Win, condition)
            colonne=input("Entrez le numero de la colonne : ")
            ligne=input("Entrez le numero de la ligne : ")
            print("Vous avez joué la case ("+colonne+","+ligne+")") 
            while grid[int(ligne)][int(colonne)]!="":
                print("Cette case est deja jouée ! Saisissez une autre case svp !")
                colonne=input("Entrez le numero de la colonne : ")
                ligne=input("Entrez le numero de la ligne : ")
                print("Vous avez joué la case ("+colonne+","+ligne+")")
            grid[int(ligne)][int(colonne)]="O"
            quelJoueur=quelJoueur-1
            
        
        displayGrid()
        
        
theGame()