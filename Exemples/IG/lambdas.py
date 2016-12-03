somme = lambda x, y: x + y  # 2 parametres : x et y, retourne x + y
print(somme(3, 4))  # Affiche : 7

somme_7_5 = lambda: somme(7, 5)  # 0 parametre, retourne somme(7, 5)
print(somme_7_5())  # Affiche : 12

a = 4
b = 5
somme_a_b = lambda: somme(a, b)  # 0 parametre mais utilisation de variables
print(somme_a_b())  # Affiche : 9
a = 10  # Modif. de variable, affectera les prochains appels de somme_a_b
print(somme_a_b())  # Affiche : 15
