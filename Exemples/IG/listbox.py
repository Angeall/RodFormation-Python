from tkinter import Tk, Variable, Listbox, Button
root = Tk()
choix = Variable(root, ('P2R-866', 
						'PJ2-445', 
						'P3X-974'))
listbox = Listbox(root, listvariable=choix, 
				  selectmode="multiple")
listbox.insert('end', 'P3X-972', 'P3X-888')
listbox.delete(2)  # Supprime le 3eme element
button = Button(root, text='Ok', 
				command=
					lambda: 
						print(listbox.curselection()))
listbox.grid(row=0, column=0)
button.grid(row=1, column=0)
root.mainloop()
