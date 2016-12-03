def read1(nom):
	fichier = open(nom)
	print(fichier.read())

def read2(nom):
	fichier = open(nom)
	ligne = fichier.readline
	while ligne != "":
		print(ligne.strip())
		ligne = fichier.readline()
	
def read3(nom):
	fichier = open(nom)
	for ligne in fichier:
		print(ligne.strip())

def ecrire(nom_de_fichier, contenu):
	fichier = open(nom_de_fichier, "x")
	fichier.write(contenu)
	fichier.close()
