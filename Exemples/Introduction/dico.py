dico = {1:"a", "abba":"musique"}
print(len(dico))                     # Affiche : 2
print(dico[1])                       # Affiche : a
print(dico["abba"])                  # Affiche : musique
dico["ma_cle"] = 42                  # Ajoute 42 a dico avec la cle 'ma_cle'


a = [("a", 1), ("b", 2), ("c", 3)]
print(dict(a))                       # Affiche : {'b': 2, 'a': 1, 'c': 3}


dico2 = {"test":42, 9+5j:"nombre complexe"}
print(list(dico2.keys()))            # Affiche : [(9+5j), 'test']
print(list(dico2.values()))          # Affiche : ['nombre complexe', 42]
print(dico2[9+5j])                   # Affiche : nombre complexe
