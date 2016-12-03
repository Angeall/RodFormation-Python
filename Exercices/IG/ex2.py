from tkinter import Tk
import tkinter.ttk as ttk
racine = Tk() 
# Definition de la fonction de changement de texte
txt = "Nombre de clic : "
counter = 0 
def changer_text():
	global counter
	counter += 1
	label['text'] = txt + str(counter)
# Creation des widgets
label = ttk.Label(racine, text=txt+str(counter), width = 30, anchor="center")
bouton = ttk.Button(text="Bouton", width = 30, command=changer_text)
# Positionnement des widgets
label.grid(column=0, row=0)
bouton.grid(column=0, row=1)
# Affichage de la fenetre
racine.mainloop()  
