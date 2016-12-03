def afficher_caractere(s, i):
	print(s[i])

def caractere(s, i):
	return s[i]
	
def caractere(s, i, j):
	return s[i:j+1]

def est_pair(nbr):
	if nbr % 2 == 0:
		return True
	return False                # Si on arrive ici, c'est qu'on a pas 
	                            #   retourne True a la ligne d'avant.
def une_lettre(s):
	if type(s) == str and len(s) == 1:
		return True
	return False
