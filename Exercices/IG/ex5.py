from tkinter import Tk, Variable, Listbox
import tkinter.ttk as ttk
import datetime	
root = Tk()
choix = Variable(root, ())
listbox = Listbox(root, listvariable=choix, width = 30, selectmode="multiple")
snap = ttk.Button(root, text='Snap',
		          command=
				    lambda: 
				      listbox.insert('end', datetime.datetime.today()))
				  
				  
				  
				  
def supprimer_tous(lstbx, selection):
	nb_supprime = 0  # Contiendra le nombre d'elements supprime
	for i in selection:  # La liste contiendra un el. de moins par suppression
		lstbx.delete(i-nb_supprime)
		nb_supprime += 1
	lstbx.select_clear(0, lstbx.size())
	
suppr = ttk.Button(root, text='Suppr',
		           command=
				     lambda: supprimer_tous(listbox, listbox.curselection()))
				
listbox.grid(row=0, column=1, columnspan=2)
snap.grid(row=1, column=0, columnspan=2)
suppr.grid(row=1, column=2, columnspan=2)
root.mainloop()
