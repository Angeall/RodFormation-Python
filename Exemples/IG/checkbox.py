from tkinter import Tk, BooleanVar
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre
var = BooleanVar()
var.set(False)
check = ttk.Checkbutton(racine, text="Exemple", 
						variable=var, width=30,
						command=
							lambda: print("quelquechose"))
check.pack()
racine.mainloop()  # Affichage de la fenetre
