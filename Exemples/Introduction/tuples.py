var = (1, 2, 3)
print(var[0])                 # Affiche : 1

var2 = var + ("a", "b", "c")  # var2 <- (1, 2, 3, 'a', 'b', 'c')

print(var2[2:5])              # Affiche : (3, 'a', 'b')

var3 = (1, (a, b))

print(var3[1])                # Affiche : ('a', 'b')
print(var3[1][0])             # Affiche : a 
                              #   car on prend l'element 0 de l'element 1

