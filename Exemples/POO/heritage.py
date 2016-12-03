class Vehicule():
	def __init__(self, marque, type_terrain, nbr_roues, vit_max):
		self.typeTerrain = type_terrain
		self.nombreRoues = nbr_roues
		self.vitesseMax = vit_max
		self.marque = marque
	
	def avoirNombreDeRoues(self):
		return self.nombreRoues
		
	def avoirMarque(self):
		return self.marque
		

class Voiture(Vehicule):
	def __init__(self, marque, vitesse_max, nbr_cv):
		# Ci-dessous l'appel au constructeur de la super-classe (parent)
		super().__init__(marque, "Route terrestre", 4, vitesse_max)
		self.nombreChevaux = nbr_cv
	
	def avoirNombreDeRoues(self):
		if super().avoirNombreDeRoues() != 4:  # Appel a la fonction parente
			print("Nombre de roues altere...")
		return 4  # Meme si l'attribut nombreRoues est altere, retourne 4
	
	def cartographier(self):
		self.nombreChevaux += 25
		
if __name__ == "__main__":
	vehicule = Vehicule("Airbus", "Aerien", 0, 1000)
	print(isinstance(vehicule, Vehicule))# Affiche : True
	print(isinstance(vehicule, Voiture)) # Affiche : False
	renault = Voiture("Renault", 140, 95)
	print(isinstance(renault, Vehicule)) # Affiche : True
	print(isinstance(renault, Voiture))  # Affiche : True
	renault.nombreRoues = 5
	print(renault.avoirNombreDeRoues())  # Affiche : Nombre de roues altere...
										 #           4
	print(renault.vitesseMax)            # Affiche : 140
	print(renault.avoirMarque())         # Affiche : Renault
	print(renault.nombreChevaux)         # Affiche : 95
	renault.cartographier()       
	print(renault.nombreChevaux)         # Affiche : 120
	
	
