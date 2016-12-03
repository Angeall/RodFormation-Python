from tkinter import Tk, Variable, Listbox
import tkinter.ttk as ttk
import datetime	
fenetre = Tk()
fenetre.geometry("300x50")
msg = "Un exemple qui prend de la place"
ttk.Style().configure("A.TLabel", background="CC0000")
label = ttk.Label(fenetre, anchor="center", text=msg, width=50)
test = ttk.Button(fenetre, text='Test')	
test2 = ttk.Button(fenetre, text='Test2')

label.grid(row=0, column=0, columnspan=2)
fenetre.grid_columnconfigure(index=0, weight=1)
fenetre.grid_columnconfigure(index=1, weight=2)
# fenetre.grid_rowconfigure(index=..., weight=...)  pour l'espace vertical
test.grid(row=1, column=0, sticky='ew') 
test2.grid(row=1, column=1, sticky='ew')  
fenetre.mainloop()
