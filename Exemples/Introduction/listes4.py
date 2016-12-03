def f(titre, *lst):
	print("titre:", titre)
	for i in lst:
		print(i)

f("Nombres", 1, 2, 3, 4)  # Affiche : titre: Nombres
                          #           1
                          #           2
                          #           3
                          #           4
