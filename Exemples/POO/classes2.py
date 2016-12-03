ma_variable = 0

class MaClasse():
	
	MA_CONSTANTE = 42
	
	def __init__(self, x, y):
		self.attribut1 = x
		self.y = y
		
	@staticmethod
	def maMethodeStatique():
		return 66
	
	def maMethode(self, monParametre):
		global ma_variable             # Indique qu'il faut utiliser la valeur 
									   #  de la variable externe "ma_variable"
		self.attribut1 = monParametre
		self.y = ma_variable
		return self.y - 1


if __name__=="__main__":
	monObjet = MaClasse("x", 55)
	print(monObjet.attribut1)              # Affiche : x
	print(monObjet.y)                      # Affiche : 55
	print(monObjet.maMethode("x2"))        # Affiche : 54
	print(monObjet.attribut1)              # Affiche : x2
	print(monObjet.y)                      # Affiche : 0
	print(monObjet.MA_CONSTANTE)           # Affiche : 42
	print(MaClasse.maMethodeStatique())    # Affiche : 66
