id = 0

class Personne():
	def __init__(self, prenom, nom, age, nationalite="Belge", metier=None):
		global id
		self.prenom = prenom
		self.nom = nom
		self.age = age
		self.nationalite = nationalite
		self.metier = metier
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
	
	def avoirStatut(self):
		if self.metier is None:
			return "Sans emploi"
		else:
			return "Employe"
	
	def demissioner(self):
		self.metier = None
		

class Fonctionnaire(Personne):
	
	def avoirStatut(self):
		if self.metier is None:
			return super().avoirStatut()
		else:
			return "Fonctionnaire"
	

class EmployeCommunal(Fonctionnaire):
	def __init__(self, prenom, nom, age, nationalite="Belge"):
		super().__init__(prenom, nom, age, "Employe communal", nationalite)
