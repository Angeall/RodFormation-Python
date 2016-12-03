import pickle

class Test():
	def __init__(self, nbr):
		self.nbr = nbr
		self.lst = []
		if nbr > 0:
			for i in range(nbr):
				self.lst.append(Test(nbr-5))
	
	def __str__(self):
		return "Test: " + str(self.nbr)
	
	def __repr__(self):   # Donne la representation par defaut en python
		return str(self)
		
if __name__ == "__main__":
	# SERIALISATION
	a = Test(5)
	b = Test(10)
	mon_fichier_a = open("serial-a.bin", mode="wb+")
	mon_fichier_b = open("serial-b.bin", mode="wb+")
	pickle.dump(a, mon_fichier_a)
	pickle.dump(b, mon_fichier_b)
	mon_fichier_a.close()
	mon_fichier_b.close()
	# DESERIALISATION
	fichier_a_lu = open("serial-a.bin", mode="rb")
	fichier_b_lu = open("serial-b.bin", mode="rb")
	a2 = pickle.load(fichier_a_lu)
	b2 = pickle.load(fichier_b_lu)
	print(a2)      # Affiche : 5
	print(a2.lst)  # Affiche : [Test: 0, Test: 0, Test: 0, Test: 0, Test: 0]
	print(b2)      # Affiche : 10
	print(b2.lst)  # Affiche : [Test: 5, Test: 5, Test: 5, ..., Test: 5]
	
