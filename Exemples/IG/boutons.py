from tkinter import Tk
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre
style = ttk.Style()
style.configure("B1.TButton", foreground="#FF0000", 
				background="#000000")
bouton1 = ttk.Button(text="Bouton 1", width = 30,
					 command=lambda: print("click b1"), 
					 style="B1.TButton")
bouton2 = ttk.Button(text="Bouton 2", width = 30,
					 command=lambda: print("click b2"))
bouton1.grid(column=0, row=0)
bouton2.grid(column=0, row=1)
racine.mainloop()  # Affichage de la fenetre
