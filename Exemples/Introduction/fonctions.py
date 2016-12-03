def ma_fonction(par1, par2=3442):  # : indique que la ligne d'apres 
							       #   a besoin d'etre indentee.
	print(par1)                   
	print(par2)                    

ma_fonction("Test")                # Affiche : Test
                                   #           3442 (par la val. par defaut)
ma_fonction(par2=5555, par1="Test")# Affiche : Test 
                                   #           5555
                                   # Car on peut preciser le parametre assigne
def div_par_2(nombre):
	var = nombre/2
	return var
	a = "3"                        # inutilisable, car apres le return

res = div_par_2(3)
print(res)                         # Affiche 1.5
#print(var)                        # Quand decommente, ceci provoquera une erreur.
                                   #   En effet, les variables crees dans une 
                                   #   fonction n'existe que dans la fonction
res2 = div_par_2(div_par_2(res))   # res2 <- ((1.5 / 2) /2) = 0.375


def calcul_inutile(qqch):
	autrechose = qqch
	autrechose /= 2
	autrechose *= 3.14

res3 = calcul_inutile(10)          # res3 <- None car il n'y a pas de return
