from tkinter import Tk
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre

ttk.Style().map("A.TButton", 
		  foreground=[("alternate", "#FF0000"), 
					  ("!disabled", "#0000FF")])

bouton1 = ttk.Button(text="Bouton 1", width = 30,
					 command=lambda: print("click b1"),
					 style="A.TButton")
bouton1.state(('active',))
bouton2 = ttk.Button(text="Bouton 2", width = 30,
					 command=lambda: print("click b2"),
					 style="A.TButton")
bouton2.state(('disabled',))
bouton3 = ttk.Button(text="Bouton 3", width = 30,
					 command=lambda: print("click b3"),
					 style="A.TButton")
bouton3.state(('focus', 'alternate'))
bouton4 = ttk.Button(text="Bouton 4", width = 30,
					 command=lambda: print("click b4"),
					 style="A.TButton")
bouton4.state(('pressed',))
bouton1.grid(column=0, row=0)
bouton2.grid(column=0, row=1)
bouton3.grid(column=0, row=2)
bouton4.grid(column=0, row=3)
racine.mainloop()  # Affichage de la fenetre
