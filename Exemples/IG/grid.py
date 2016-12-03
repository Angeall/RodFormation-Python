from tkinter import Tk, Variable, Listbox
import tkinter.ttk as ttk
import datetime	
root = Tk()
root.geometry("300x50")
msg = "Un exemple qui prend de la place"
ttk.Style().configure("A.TLabel", background="CC0000")
label = ttk.Label(root, anchor="center", text=msg, width=50)
test = ttk.Button(root, text='Test')	
test2 = ttk.Button(root, text='Test2')
label.grid(row=0, column=0, columnspan=2)
# Colle Test a droite
test.grid(row=1, column=0, sticky='e')  
# Colle Test2 a gauche
test2.grid(row=1, column=1, sticky='w')  
root.mainloop()
