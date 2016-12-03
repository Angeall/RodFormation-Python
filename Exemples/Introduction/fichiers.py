fichier = open("test.txt")        # Ouvre le fichier 
                                  #     mode : lecture texte (defaut)
texte_entier = fichier.read()     # Lit le texte en entier
print("texte entier:\n" + texte_entier + "\n")
 
fichier = open("test.txt")
texte_partiel = fichier.read(10)  # Lit 10 caracteres du fichier
print("10 premier caracteres:\n" + texte_partiel + "\n")

fichier = open("test.txt")
premiere_ligne = fichier.readline()
deuxieme_ligne = fichier.readline()

fichier = open("test.txt")
i = 0
for ligne in fichier:
	# end = "" annule le retour a la ligne par defaut
	print("ligne " + str(i) + " : " + ligne, end = "") 
	i += 1
