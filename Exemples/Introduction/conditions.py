if 3 < 4:                             # La comparaison sera toujours vraie
	print ("3 est plus petit que 4")  # Affiche : 3 est plus petit que 4
else:                                 # Jamais execute car 3 < 4...
	print ("le monde est fou !")

var = "ab"
var2 = "aba"

if var == var2:                       # Faux car "ab" != de "aba"
	print ("ah bon?")                 
elif var == var2[0:2]:                # Vrai car "ab" == "ab"
	print ("ca c'est vrai")			  # Affiche : ca c'est vrai

var = "aab"
var2 = "ab"

if var[0] == var2[0]:                 # Vrai car "a" == "a"  
	print("ok")                       # Affiche : ok
if var[1] == var2[0]:                 # Vrai car "a" == "a"
	print("ok aussi")                 # Affiche : ok aussi
elif var[2] == var2[1]:               # Condition vraie, mais c'est un 
	print("et non ...")               # sinon si, et la condition precedente
	                                  # etait vraie...
var = "je suis" in "je suis la"       # var <- True                            


var = 3 < 4 and "aa" == "bb"          # var <- False parce que "aa" != "bb"
var = 3 < 4 or "aa" == "bb"           # var <- True parce que 3 < 4 == True
var = not 4 < 3                       # var <- True parce que 4 < 3 == False


var = (3 < 4 and "aa" == "bb") or 'a' == 'a'  # var <- True car 'a' == 'a'
