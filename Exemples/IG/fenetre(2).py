from tkinter import Tk, Toplevel
parent = Tk()
parent.title('parent')
parent.geometry('200x200+0+0')  # Fenetre 200x200 en haut a gauche de l'ecran
parent.resizable(True, False)  # Redimensionnement horizontal uniquement
enfant = Toplevel(parent) 
enfant.title('enfant')
enfant.geometry('150x150-0+0')  # Apparition en haut a droite de l'ecran
enfant.transient(parent)  # Enfant lie au parent
parent.mainloop()
