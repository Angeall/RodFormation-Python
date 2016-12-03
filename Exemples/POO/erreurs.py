class MonException(Exception):
	pass
	

def divise(nbr, diviseur):
	if not (type(nbr) == int or type(nbr) == float) or \
		  not (type(diviseur) == int or type(diviseur) == float):
		raise MonException("Des nombres sont attendus en parametres")
	return nbr / diviseur

if __name__ == "__main__":
	try:
		divise("", 4)
	except MonException:
		print("Erreur: divise ne prend que des nombres en parametres")
	finally:
		print("Test 1 termine")
	
	try:
		divise(5, 0)
	except ZeroDivisionError:
		print("Erreur: diviseur doit etre different de 0")
	finally:
		print("Test 2 termine")
		
	try:
		divise("", 4)
	except ZeroDivisionError:   # Ne se produit pas
		print("Erreur: diviseur doit etre different de 0")
	except:                     # Se produit car attend n'importe quelle exception
		print("Une erreur s'est produite")
	finally:
		print("Test 3 termine")
	
	try:
		divise(3, 4)
	except:                     # Aucune erreur ne se produit
		print("Une erreur s'est produite")
	finally: 
		print("Test 4 termine") # Le message dans le finally s'affiche quand meme
	
	
	
