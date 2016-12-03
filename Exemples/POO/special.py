class Test():
	def __init__(self, nbr):
		self.nbr = nbr
	
	def __str__(self):
		return "Nombre: " + str(self.nbr)
		
	def __add__(self, other):
		if type(other) == type(self):  # Si l'autre objet est un objet Test
			return Test(self.nbr + other.nbr)
		elif type(other) == int:
			return Test(self.nbr + other)
	
	def __radd__(self, other):
		if type(other) == type(self):  # Si l'autre objet est un objet Test
			return Test(self.nbr + other.nbr)
		elif type(other) == int:
			return Test(self.nbr + other)
		else: 
			return None
		
		
if __name__ == "__main__":
	a = Test(3)
	print(a)       # Affiche : Nombre: 3
	b = Test(5)
	print(a + b)   # Affiche : Nombre: 8
	print(a + 10)  # Affiche : Nombre: 13
	# __radd__ est necessaire pour que le prochain test fonctionne
	print(10 + b)  # Affiche : Nombre: 15
	
	
