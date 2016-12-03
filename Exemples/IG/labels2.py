from tkinter import Tk
import tkinter.ttk as ttk  # Abreviation de l'import
racine = Tk()  # Creation de la fenetre

label = ttk.Label(racine, anchor="center", 
				  text="Hello World")
label2 = ttk.Label(racine, text="Hello World")
label3 = ttk.Label(racine, text="Hello World")
label.grid(column=0, row=0, columnspan=2)
label2.grid(column=0, row=1)
label3.grid(column=1, row=1)

racine.mainloop()  # Affichage de la fenetre
