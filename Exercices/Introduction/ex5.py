from ex4 import est_pair, afficher_caractere

def somme_range(nbr):
	somme = 0
	for i in range(nbr+1):
		somme += i
	return somme

def afficher_pair(s):
	for i in range(len(s)):
		if est_pair(i):
			afficher_caractere(s, i)		

def est_palyndrome(s):
	i = 0
	for j in range(len(s)-1, -1, -1):
		if s[i] != s[j]:
			return False
		i += 1
	return True




def multiplie_par_9(n):
	i = 0
	somme = 0
	while i < 9:
		somme += n
		i += 1
	return str(somme)
