from tkinter import Tk, StringVar
import tkinter.ttk as ttk
# Creation de la fenetre
fenetre = Tk()
fenetre.title("exo1.py")
# Definition des styles
style = ttk.Style()
style.configure("Titre.TLabel", font="Helvetica 14 bold", 
				foreground="#801515", padding=(125, 0))
style.configure("SousTitre.TLabel", font=("Helvetica", 12), 
				foreground="#AA3939", padding=(0, 0, 0, 20))
style.configure("Paragraphe.TLabel", font="Helvetica 11 underline", 
				foreground="#D46A6A", padding=(0, 0, 0, 8))
# Creation des widgets
titre = ttk.Label(fenetre, text="Titre", style="Titre.TLabel", anchor="center")
soustitre = ttk.Label(fenetre, text="Sous-Titre", style="SousTitre.TLabel", 
					  anchor="center")
par = ttk.Label(fenetre, text="Paragraphe 1", style="Paragraphe.TLabel")
texte = ttk.Label(fenetre, text="Lorem ipsum [...] ")
texte2 = ttk.Label(fenetre, text="Quelque chose 1")
texte3 = ttk.Label(fenetre, text="Quelque chose 2")
# Positionnement des widgets
titre.grid(column=0, row=0, columnspan=2)
soustitre.grid(column=0, row=1, columnspan=2)
par.grid(column=0, row=2)
texte.grid(column=0, row=3, rowspan=2)
texte2.grid(column=1, row=3)
texte3.grid(column=1, row=4)
# Lancement de la fenetre
fenetre.mainloop()
