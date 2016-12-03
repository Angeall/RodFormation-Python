mon_entier = 9                # type: <class 'int'>
mon_complexe = 5 + 9j         # type: <class 'complex'>
mon_complexe = complex(5, 9)  # Equivalent a la ligne precedente
mon_float = 10.5              # type: <class 'float'>


res  = mon_float // 2         # res  <- 10.5 div. entier. par 2 = 5.0
res2 = mon_entier // 2        # res2 <- 9 div. entiere par 2 = 4
res3 = mon_entier / 2         # res3 <- 9 / 2 = 4.5 (devient un float)
res4 = mon_entier * 3         # res4 <- 9 * 3 = 27
res5 = mon_entier + 1         # res5 <- 9 + 1 = 10
res6 = mon_entier - 2         # res6 <- 9 - 2 = 7
res7 = mon_entier % 2         # res7 <- reste div. ent. de 9 par 2 = 1
res8 = 0
res8 += 1                     # res8 <- res8 + 1 = 0 + 1 = 1
res8 *= 4                     # res8 <- res8 * 4 = 1 * 4 = 4
res8 /= 2                     # res8 <- res8 / 2 = 4 / 2 = 2
res8 -= 2                     # res8 <- res8 - 2 = 2 - 2 = 0
res9 = mon_entier ** 2        # res9 <- 9 puissance 2 = 81
test = int(mon_float)         # test <- partie entiere de 10.5 = 10
test = str(mon_float)         # test <- "10.5"
