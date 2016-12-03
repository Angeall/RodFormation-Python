from tkinter import Tk, StringVar
import tkinter.ttk as ttk
racine = Tk()  # Creation de la fenetre
var = StringVar()
var.set("Groupe1: Choix A")
radio1 = ttk.Radiobutton(racine, variable=var, 
						text= "Groupe1: Choix A", 
						width=30,
						value = "Groupe1: Choix A",
						command=
							lambda: print("radio1"))
radio2 = ttk.Radiobutton(racine, variable=var, 
						text="Groupe1: Choix B", 
						width=30,
						value = "Groupe1: Choix B",
						command=
							lambda: print("radio2"))
var2 = StringVar()
var2.set("Groupe2: Choix A")
radio3 = ttk.Radiobutton(racine, variable=var2, 
						text= "Groupe2: Choix A", 
						width=30,
						value = "Groupe2: Choix A",
						command=
							lambda: print("radio3"))
radio1.pack()
radio2.pack()
radio3.pack()
racine.mainloop()  # Affichage de la fenetre
