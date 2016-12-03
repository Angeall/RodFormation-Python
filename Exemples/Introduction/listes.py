lst = [1, "a", 3]
lst[1] = 2         # lst devient [1, 2, 3]

lst[:] = ["a"]     # lst devient ['a'] => on remplace tous les elements


lst = ["a"]
lst2 = lst         # lst2 <- ['a'] (mais ca reste la meme liste que lst!)
lst2[0] = "b"      # lst2 devient ['b'], mais lst aussi !
print(lst2, lst)   # Affiche : ['b'] ['b']
