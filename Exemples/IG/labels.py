from tkinter import Tk
# as = Abreviation de l'import
import tkinter.ttk as ttk  
racine = Tk()  # Creation de la fenetre
# Cree le label, attache a la fenetre racine
label = ttk.Label(racine, text="Hello World") 
label.grid()  # Place le label sur la fenetre

racine.mainloop()  # Affichage de la fenetre
