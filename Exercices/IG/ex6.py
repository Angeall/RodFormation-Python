from tkinter import Tk, Toplevel
import tkinter.ttk as ttk
root = Tk()

def lancer_erreur(msg):
	global root
	popup = Toplevel(root)
	popup.transient(root)
	err_label = ttk.Label(popup, text=msg)
	err_label.pack()

erreur = ttk.Button(root, text='Erreur',
		            command=
				      lambda: 
				        lancer_erreur("Vous avez clique sur le bouton Erreur"))
				  
def supprimer_tous(lstbx, selection):
	for i in selection:
		lstbx.delete(i)
	lstbx.select_clear(0, lstbx.size())
	
replacer = ttk.Button(root, text='Replacer',
		              command=
				        lambda: root.geometry('640x480+0-0'))
				
erreur.grid(row=0, column=0, columnspan=2)
replacer.grid(row=0, column=2, columnspan=2)
root.mainloop()
