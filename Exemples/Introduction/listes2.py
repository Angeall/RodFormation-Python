lst = [["a"], 3]
lst2 = lst.copy()
lst[0][0] = "b"        # La liste interne est modifiee dans les 2 variables
lst[1] = 4             # L'element est modifie uniquement dans lst 
                       #     car il n'est pas dans une liste interne
print(lst)             # Affiche : [["b"], 4]
print(lst2)            # Affiche : [["b"], 3]


from copy import deepcopy

lst3 = [["a"], 3]
lst4 = deepcopy(lst3)  # La liste interne est entierement copiee
lst3[0][0] = "b"
lst3[1] = 4
print(lst3)            # Affiche : [["b"], 4]
print(lst4)            # Affiche : [["a"], 3]
