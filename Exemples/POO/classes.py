class MaClasse():
	pass          # pass signifie juste que l'on ne fait rien du tout


if __name__=="__main__":
	monObjet = MaClasse()
	print(monObjet.__dir__())     # Affiche toutes les methodes de l'objet :
								  #  heritees, ou crees par la classe
	print(monObjet.__sizeof__())  # Affiche la taille, en octets, de l'objet
	print(monObjet.__str__())     # Affiche la representation par defaut 
								  #  de notre objet en chaine de caracteres
