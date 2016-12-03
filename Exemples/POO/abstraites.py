from abc import ABCMeta, abstractmethod

class Vehicule(metaclass=ABCMeta):
		
	@property
	@abstractmethod
	def nombreDeRoues(self):
		return 0
	
	@abstractmethod
	def demarrer(self):
		pass             
		

class Voiture(Vehicule):
	def __init__(self):
		self._qqch = None
		self.contact = False
	
	@property
	def nombreDeRoues(self):
		print("Vehicule:", super().nombreDeRoues)  
		return 4
	
	@property
	def plaqueImmatriculation(self):
		return self._qqch
	
	@plaqueImmatriculation.setter
	def plaqueImmatriculation(self, valeur):
		if type(valeur) == str:
			self._qqch = valeur
	
	def demarrer(self):
		self.contact = True	
	
		
if __name__ == "__main__":
	renault = Voiture()
	renault.nombreRoues = 5                    # Ne fait rien car pas de setter
	print(renault.nombreDeRoues)               # Affiche : Vehicule: 0
	                                           # Affiche : 4
	print(renault.plaqueImmatriculation)       # Affiche : None
	renault.plaqueImmatriculation = 123        
	print(renault.plaqueImmatriculation)       # Affiche : None
	renault.plaqueImmatriculation = "1ABC123" 
	print(renault.plaqueImmatriculation)       # Affiche : 1ABC123
	
