from tkinter import Tk, StringVar
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre

ttk.Style().map("A.TEntry", 
		  foreground=[("disabled", "#FF0000"), 
					  ("!disabled", "#000000")])
var = StringVar()
var.set("Texte de base")
entry = ttk.Entry(racine, textvariable=var, style="A.TEntry",
				  justify="center", width=30)

bouton1 = ttk.Button(racine, text="Afficher texte", 
					command=lambda: print(var.get()), width=30)
titre_b2 = StringVar()
titre_b2.set("Desactiver champs de saisie")

i = 0
def changer_etat():
	global i, entry
	i += 1
	if i%2 == 0:
		titre_b2.set("Desactiver champs de saisie")
		entry.state(("!disabled",))
	else:
		titre_b2.set("Activer champs de saisie")
		entry.state(("disabled",))

bouton2 = ttk.Button(racine, textvariable=titre_b2, 
					 command=changer_etat, width=30)
entry.pack()
bouton1.pack()
bouton2.pack()
racine.mainloop()  # Affichage de la fenetre
