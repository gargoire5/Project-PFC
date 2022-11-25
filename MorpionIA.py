grid=[[" "," "," "],[" "," "," "],[" "," "," "]]

lignechoisie=2
colonnechoisie=1



def displayGrid():
    print (grid[0])
    print (grid[1])
    print (grid[2])

def CheckWin(quelJoueur, gagnant, conditionWin):
    if (grid[0][0]==grid[0][1] and grid[0][0]==grid[0][2] and grid[0][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True  
            displayGrid()     
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[0][0]==grid[1][0] and grid[0][0]==grid[2][0] and grid[0][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[0][0]==grid[1][1] and grid[0][0]==grid[2][2] and grid[0][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid()
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()
    if (grid[2][0]==grid[1][1] and grid[2][0]==grid[0][2] and grid[2][0]!=" "):
        if quelJoueur==1:
            print("Le joueur 2 a gagné!!!")
            conditionWin = True
            displayGrid() 
        if quelJoueur==2:
            print("L'ia a gagné!!!")
            conditionWin = True
            displayGrid()

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
        if quelJoueur==1:
            quelJoueur=quelJoueur+1
            nbTour=nbTour + 1
            if nbTour==1:
                grid[1][1]="X"
                if (CheckWin(quelJoueur, Win, conditionWin) == True):
                    break;
            if nbTour==3:
                if grid[0][0] == " " and grid[2][2] == " ":
                    grid[0][0]="X"
                else:
                    if grid[2][0]==" " and grid[0][2]== " ":
                        grid[2][0]="X"
                if (CheckWin(quelJoueur, Win, conditionWin) == True):
                    break;
            if nbTour==5:
                if grid[0][0]=="X" and grid [2][2]==" ":
                    grid[2][2]="X"
                elif grid[0][2]==" " and grid [2][0]=="X":
                    grid[0][2]="X"
                else:
                    if grid[0][0]=="O" and grid[0][1]=="O":
                        grid[0][2]="X"
                    elif grid[0][1]=="O" and grid[0][2]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[0][2]=="O":
                        grid[0][1]="X"
                    elif grid[0][0]=="O" and grid[1][0]=="O":
                        grid[2][0]="X"
                    elif grid[1][0]=="O" and grid[2][0]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[2][0]=="O":
                        grid[1][0]="X"
                    elif grid[0][2]=="O" and grid[1][2]=="O":
                        grid[2][2]="X"
                    elif grid[1][2]=="O" and grid[2][2]=="O":
                        grid[0][2]="X"
                    elif grid[0][2]=="O" and grid[2][2]=="O":
                        grid[1][2]="X"
                    elif grid[2][0]=="O" and grid[2][1]=="O":
                        grid[2][2]="X"
                    elif grid[2][1]=="O" and grid[2][2]=="O":
                        grid[2][0]="X"
                    elif grid[2][0]=="O" and grid[2][2]=="O":
                        grid[2][1]="X"
                    elif grid[0][0]==" ":
                        grid[0][0]="X"
                    elif grid[0][2]==" ":
                        grid[0][2]="X"
                    elif grid[2][2]==" ":
                        grid[2][2]="X"
                    elif grid[2][0]==" ":
                        grid[2][0]="X"
                    elif grid[0][1]==" ":
                        grid[0][1]="X"
                    elif grid[1][0]==" ":
                        grid[1][0]="X"
                    elif grid[1][2]==" ":
                        grid[1][2]="X"
                    elif grid[2][1]==" ":
                        grid[2][1]="X"
                if (CheckWin(quelJoueur, Win, conditionWin) == True):
                    break;
            if nbTour==7:
                if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][1]=="X" and grid[0][2]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][0]=="X" and grid[0][2]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[1][0]=="X" and grid[2][0]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][0]=="X" and grid[2][0]=="X" and grid[1][0]==" ":
                    grid[1][0]="X"
                elif grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[1][2]=="X" and grid[2][2]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][2]=="X" and grid[2][2]=="X" and grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[2][1]=="X" and grid[2][2]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[2][0]=="X" and grid[2][2]=="X" and grid[2][1]==" ":
                    grid[2][1]="X"
                elif grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]==" ":
                    grid[2][1]="X"
                elif grid[1][1]=="X" and grid[2][1]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[1][1]=="X" and grid[1][2]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[1][1]=="X" and grid[2][2]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[1][1]=="X" and grid[2][0]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[1][0]==" ":
                    grid[1][0]="X"
                elif grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[2][1]=="X":
                    grid[2][1]="X"
                else:
                    if grid[0][0]=="O" and grid[0][1]=="O":
                        grid[0][2]="X"
                    elif grid[0][1]=="O" and grid[0][2]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[0][2]=="O":
                        grid[0][1]="X"
                    elif grid[0][0]=="O" and grid[1][0]=="O":
                        grid[2][0]="X"
                    elif grid[1][0]=="O" and grid[2][0]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[2][0]=="O":
                        grid[1][0]="X"
                    elif grid[0][2]=="O" and grid[1][2]=="O":
                        grid[2][2]="X"
                    elif grid[1][2]=="O" and grid[2][2]=="O":
                        grid[0][2]="X"
                    elif grid[0][2]=="O" and grid[2][2]=="O":
                        grid[1][2]="X"
                    elif grid[2][0]=="O" and grid[2][1]=="O":
                        grid[2][2]="X"
                    elif grid[2][1]=="O" and grid[2][2]=="O":
                        grid[2][0]="X"
                    elif grid[2][0]=="O" and grid[2][2]=="O":
                        grid[2][1]="X"
                if (CheckWin(quelJoueur, Win, conditionWin) == True):
                    break;
            if nbTour==9:
                if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][1]=="X" and grid[0][2]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][0]=="X" and grid[0][2]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[1][0]=="X" and grid[2][0]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][0]=="X" and grid[2][0]=="X" and grid[1][0]==" ":
                    grid[1][0]="X"
                elif grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[1][2]=="X" and grid[2][2]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][2]=="X" and grid[2][2]=="X" and grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[2][1]=="X" and grid[2][2]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[2][0]=="X" and grid[2][2]=="X" and grid[2][1]==" ":
                    grid[2][1]="X"
                elif grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]==" ":
                    grid[2][1]="X"
                elif grid[1][1]=="X" and grid[2][1]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[1][1]=="X" and grid[1][2]=="X" and grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[1][1]=="X" and grid[2][2]=="X" and grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[1][1]=="X" and grid[2][0]=="X" and grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[0][0]==" ":
                    grid[0][0]="X"
                elif grid[0][2]==" ":
                    grid[0][2]="X"
                elif grid[2][2]==" ":
                    grid[2][2]="X"
                elif grid[2][0]==" ":
                    grid[2][0]="X"
                elif grid[0][1]==" ":
                    grid[0][1]="X"
                elif grid[1][0]==" ":
                    grid[1][0]="X"
                elif grid[1][2]==" ":
                    grid[1][2]="X"
                elif grid[2][1]==" ":
                    grid[2][1]="X"
                else:
                    if grid[0][0]=="O" and grid[0][1]=="O":
                        grid[0][2]="X"
                    elif grid[0][1]=="O" and grid[0][2]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[0][2]=="O":
                        grid[0][1]="X"
                    elif grid[0][0]=="O" and grid[1][0]=="O":
                        grid[2][0]="X"
                    elif grid[1][0]=="O" and grid[2][0]=="O":
                        grid[0][0]="X"
                    elif grid[0][0]=="O" and grid[2][0]=="O":
                        grid[1][0]="X"
                    elif grid[0][2]=="O" and grid[1][2]=="O":
                        grid[2][2]="X"
                    elif grid[1][2]=="O" and grid[2][2]=="O":
                        grid[0][2]="X"
                    elif grid[0][2]=="O" and grid[2][2]=="O":
                        grid[1][2]="X"
                    elif grid[2][0]=="O" and grid[2][1]=="O":
                        grid[2][2]="X"
                    elif grid[2][1]=="O" and grid[2][2]=="O":
                        grid[2][0]="X"
                    elif grid[2][0]=="O" and grid[2][2]=="O":
                        grid[2][1]="X"
            if (CheckWin(quelJoueur, Win, conditionWin) == True):
                break;
        if nbTour==9:
            print("Egalité")
            displayGrid()
            break;
        if quelJoueur==2:
            displayGrid()
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
   


     
theGame(False)