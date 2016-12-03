id = 0

class Personne():
	def __init__(self, prenom, nom, age, nationalite="Belge"):
		global id
		self.prenom = prenom
		self.nom = nom
		self.age = age
		self.nationalite = nationalite
		self.id_conjoint = None
		self.id = id
		id += 1
		
	def vieillir(self, age=1):
		self.age += age
	
	def expatrier(self, nationalite):
		self.nationalite = nationalite
	
	def marier(self, id_conjoint):
		self.id_conjoint = id_conjoint
		
	def divorcer(self):
		self.id_conjoint = None
	
	def estMarie(self):
		return self.id_conjoint is not None
