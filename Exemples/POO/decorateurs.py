def mon_decorateur_majuscule(fct):
	def cadre(chaine):
		return fct(chaine).upper()
	return cadre
	
@mon_decorateur_majuscule
def ajout1(chaine):
	return chaine + "_old"
	
@mon_decorateur_majuscule
def ajout2(chaine):
	return chaine + "_deprecated"

def ajout3(chaine):
	return chaine + "_new"
	
if __name__ == "__main__":
	print(ajout1("Richard"))  # Affiche : RICHARD_OLD
	print(ajout2("Test"))     # Affiche : TEST_DEPRECATED
	print(ajout3("Protoss"))  # Affiche : Protoss_new
