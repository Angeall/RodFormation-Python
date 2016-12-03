from tkinter import StringVar, Tk
import tkinter.ttk as ttk
fenetre = Tk()  # Creer la fenetre
# Configuration de la spinbox
var = StringVar()
choix = ["test1", "test2", "test3", "test4"]
combobox = ttk.Combobox(fenetre, values=choix, 
					    textvariable=var,
					    postcommand=
						  lambda: print(var.get()))
combobox.bind('<<ComboboxSelected>>', 
			  lambda x: print(combobox.get()))
combobox.pack()
fenetre.mainloop()  # Lancement de la fenetre
