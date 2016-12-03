from tkinter import StringVar, Tk
Tk()  # Requis pour que les Variables tkinter fonctionnent
var = StringVar()
var.set("Une chaine")
print(var.get())  # Affiche : Une chaine
