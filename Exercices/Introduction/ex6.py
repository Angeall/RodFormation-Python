def duree(debut, fin):
	(heures_debut, minutes_debut) = debut
	(heures_fin, minutes_fin) = fin
	minutes_totales_debut = (heures_debut * 60) + minutes_debut
	minutes_totales_final = (heures_fin * 60) + minutes_fin
	diff = minutes_totales_final - minutes_totales_debut
	if diff < 0: 
		diff = diff + (24 * 60)
	minutes = diff % 60
	heures = diff//60 
	return (heures, minutes)

def duree2(debut,fin):
	(heures_debut, minutes_debut) = debut
	(heures_fin, minutes_fin) = fin
	minutes_totales_debut = (heures_debut * 60) + minutes_debut
	minutes_totales_final = (heures_fin * 60) + minutes_fin
	diff = minutes_totales_final - minutes_totales_debut
	minutes = diff % 60
	heures = (diff // 60) % 24
	return (heures, minutes)
	
def insertion_triee(lst, nbr):
	indice = 0
	for i in lst:
		if i <= nbr:              # Sinon, on a trouve l'indice auquel inserer
			indice += 1
	lst[:] = lst[:indice] + [nbr] + lst[indice:]  # On modifie la liste
	
def insertion_triee_avec_break(lst, nbr):
	indice = 0
	for i in lst:
		if i > nbr:              # On a trouve l'indice auquel inserer
			break                # Arrete la boucle
		indice += 1
	lst[:] = lst[:indice] + [nbr] + lst[indice:]  # On modifie la liste
