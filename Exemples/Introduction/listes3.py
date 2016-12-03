lst = []             # lst <- liste vide
lst.append(3)        # lst <- liste vide + 3 = [3]
lst.append("abba")   # lst <- [3] + "abba" = [3, 'abba']
print(len(lst))      # Affiche : 2 car il y a 2 elements dans lst
var = lst.pop()      # var <- 'abba' et lst <- [3]
print(len(lst))      # Affiche : 1 car il ne reste qu'un element dans lst


lst2 = ["a", "b", "d", "e"]
lst2.insert(2, "c")
print(lst2)                  # Affiche : ["a", "b", "c", "d", "e"]

