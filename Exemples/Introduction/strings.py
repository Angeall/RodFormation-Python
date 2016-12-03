var = ""  # chaine vide
var = ''  # chaine vide aussi (pas de differences entre '...' et "...")


var = "je suis une chaine"  # Les chaines sont indicee de 0 a la taille - 1
partie = var[0]             # partie <- Premier caractere de var = "j"
partie = var[5]             # partie <- Sixieme caractere de var = "i"
partie = var[3:7]           # partie <- var du 4 au 7eme car. = "suis"
                            #           (8eme caractere non compris)
partie = var[:7]            # partie <- du 1er car. au 7eme = "je suis"
partie = var[-1]            # partie <- le dernier caractere = "e"
partie = var[3:]            # partie <- du 3eme car. a la fin = "suis..."


repetition = "lala" * 3     # repetition <- "lalalalalala"
concatenation = "AB" + "BA" # concatenation <- "ABBA"


ma_chaine = "\\"
print(ma_chaine)            # Affiche \ car on despecialise le caract. "\"


var = "C\'est ma chaine"   
print(var.upper())            # Affiche C'EST MA CHAINE (sans modif. var)
print(var.lower())            # Affiche c'est ma chaine (sans modif. var)
var2 = var.replace("e", "x")  # var2 <- C'xst ma chainx (sans modif. var)
print(var2)                   # Affiche C'xst ma chainx
var3 = "Ma\nChaine\n"
print(var3)	                  # Affiche Ma
                              #         Chaine
                              #         		=> (\n de fin de ligne)
print(var3.strip())           # Affiche Ma
                              #         Chaine
print("une chaine".isalpha()) # Affiche False a cause de l'espace
print("une".isalpha())        # Affiche True car chaque car. est une lettre
print("012".isdigit())        # Affiche True car chaque car. est un chiffre
