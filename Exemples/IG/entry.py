from tkinter import Tk, StringVar
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre
var = StringVar(value="A modifier")
entry = ttk.Entry(racine, textvariable=var,
				  justify="center", width=30)
entry.pack()
racine.mainloop()  # Affichage de la fenetre
