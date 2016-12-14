import string
import random
import datetime	
from abc import ABCMeta, abstractmethod

id = 0

def sauver_changement_nationalite(fct):
	def sauver_expatriement(self, nationalite):
		old = self.nationalite
		fct(self, nationalite)
		new = self.nationalite
		msg = old  + " -> " + new + " : " + str(datetime.date.today())
		self.nationalites.append(msg)
	return sauver_expatriement





class Personne(metaclass=ABCMeta):
	def __init__(self, prenom, nom, age, nationalite="Belge", metier=None):
		global id
		self.prenom = prenom
		self.nom = nom
		self.age = age
		self.nationalite = nationalite
		self.metier = metier
		self.nationalites = []
		self.id_conjoint = None
		self.id = id
		id += 1
	
	@property
	@abstractmethod
	def sexe(self):
		pass
		
	def vieillir(self, age=1):
		self.age += age
	
	@sauver_changement_nationalite
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
	
	def __str__(self):
		return self.nom + " " + self.prenom + ", " + str(self.age) + " ans."
		
		
	def __add__(self, other):
		if isinstance(other, Personne):
			self.marier(other.id)
			other.marier(self.id)
	
	def __mul__(self, other):
		if type(other) == int:
			lst = []
			for i in range(other):
				prenom = random.choice(string.ascii_uppercase)
				for i in range(random.randint(2, 7)):
					prenom += random.choice(string.ascii_lowercase)
				sexe = random.randint(0, 9)  # MODIFIE POUR RESPECTER CLASSE ABSTRAITE
				if sexe < 5:
					lst.append(Homme(prenom, self.nom, 0, self.nationalite))
				else:
					lst.append(Femme(prenom, self.nom, 0, self.nationalite))
			return lst			
		else:
			return None
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __lt__(self, other):
		if type(other) == type(self):
			if self.nom == other.nom:
				return self.prenom < other.prenom
			else:
				return self.nom < other.nom
				
	def __le__(self, other):
		if type(other) == type(self):
			if self.nom == other.nom:
				return self.prenom <= other.prenom
			else:
				return self.nom <= other.nom
	
	def __gt__(self, other):
		if type(other) == type(self):
			if self.nom == other.nom:
				return self.prenom > other.prenom
			else:
				return self.nom > other.nom	
	
	
	
	def __ge__(self, other):
		if type(other) == type(self):
			if self.nom == other.nom:
				return self.prenom >= other.prenom
			else:
				return self.nom >= other.nom	
		
	def __eq__(self, other):
		if type(other) == type(self):
			return self.nom == other.nom and self.prenom == other.prenom

class Homme(Personne):
	@property 
	def sexe(self):
		return "Homme"

class Femme(Personne):
	@property
	def sexe(self):
		return "Femme"	

