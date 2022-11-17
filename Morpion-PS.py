from random import randint


grid = []

def emptyGrid():
	for i in range (3):
		row = []
		for j in range (3):
			row.append('-')
		grid.append(row)

	for row in grid:
		for item in row:
			print(item, end=" ")
		print()

def startGame():
	print("Bienvenue sur le morpion vous allez jouer face a une IA, vous allez jouer les X")
	print("Pour jouer...")
	emptyGrid()

	Win=0
	while Win!=1:
		colonne=input("Entrez le numero de la colonne : ")
		ligne=input("Entrez le numero de la ligne : ")
		print("Vous avez joué la case ("+colonne+","+ligne+")")
		while grid[int(ligne)][int(colonne)]!="-":
			print("Cette case est deja jouée ! Saisissez une autre case svp !")
			colonne=input("Entrez le numero de la colonne : ")
			ligne=input("Entrez le numero de la ligne : ")
			print("Vous avez joué la case ("+colonne+","+ligne+")")
		grid[int(ligne)][int(colonne)]="X"
		emptyGrid()
		if (grid[0][0]==grid[0][1] and grid[0][0]==grid[0][2] and grid[0][0]!=" "):
			Win=1
		if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
			Win=1
		if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
			Win=1
		if (grid[0][0]==grid[1][0] and grid[0][0]==grid[2][0] and grid[0][0]!=" "):
			Win=1
		if (grid[1][0]==grid[1][1] and grid[1][0]==grid[1][2] and grid[1][0]!=" "):
			Win=1
		if (grid[2][0]==grid[2][1] and grid[2][0]==grid[2][2] and grid[2][0]!=" "):
			Win=1
		if (grid[0][0]==grid[1][1] and grid[0][0]==grid[2][2] and grid[0][0]!=" "):
			Win=1
		if (grid[2][0]==grid[1][1] and grid[2][0]==grid[0][2] and grid[2][0]!=" "):
			Win=1
startGame()
