def recup_element(dico, cle):
	if cle in dico.keys():
		return dico[cle]
	return None

def liste_vers_dico(lst):
	for couple in lst:
		if not(type(couple) == tuple and len(couple) == 2):
			return None
	return dict(lst)
