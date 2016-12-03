from tkinter import Tk, Listbox, StringVar, BooleanVar, Toplevel
import tkinter.ttk as ttk
import datetime	
from bdp import *  # Importe la classe BaseDePersonnes se trouvant dans bdp.py
root = Tk()
root.title("BaseDePersonnes")

bdp = None  # Contiendra la BaseDePersonnes
ids = {}  # Un dictionnaire qui liera les indices de la listbox aux ID des pers.

# Lance un popup d'erreur
def popup_erreur(parent, msg):  # Cree un popup d'erreur
	popup = Toplevel(parent)
	popup.title("Erreur")
	popup.transient(parent)
	err_label = ttk.Label(popup, text=msg)
	err_label.pack()
	err_bouton = ttk.Button(popup, text="OK", command=lambda: popup.destroy())
	err_bouton.pack()

# Cree un label suivi d'un champs d'entree de texte
def entry_avec_label(parent, txt, stringvar, column, row):
	frame = ttk.Frame(parent)
	label = ttk.Label(frame, text=txt, width=15)
	entry = ttk.Entry(frame, textvariable=stringvar)
	label.grid(column=0, row=0)
	entry.grid(column=1, row=0)
	frame.grid(column=column, row=row)





# Cree des champs de selection
def creer_radios(parent, texts, stringvar, column, row):
	frame = ttk.Frame(parent)
	i = 0
	for txt in texts:
		radio = ttk.Radiobutton(frame, text=txt, value=txt, variable=stringvar)
		radio.grid(row=0, column=i)
		i += 1
	frame.grid(column=column, row=row)


# Efface toutes les entrees de la listes
def nettoyer_liste(liste):
	global ids
	ids = {}  # Nettoie le dictionnaire
	liste.delete(0, 'end')  # Nettoie la liste

# Affiche les personnes de la base de donnees
def update_liste(liste):  
	global bdp, ids
	personnes = bdp.recuperer_tous()
	nettoyer_liste(liste)
	i = 0
	for personne in personnes:
		ids[i] = personne.id
		liste.insert('end', str(personne))
		i+=1
	
# Ajoute une persone dans la bdd et dans la liste
def ajouter_personne(liste, prenom, nom, age, homme, nationalite, metier):
	id = bdp.ajouter(prenom, nom, age, homme, nationalite, metier)
	personne = bdp.recuperer(id)
	liste.insert('end', str(personne))
	ids[len(ids)] = id
	return bdp

# Supprime des personnes dans la liste
def supprimer_personnes(liste, indices):
	global bdp, ids
	if bdp is not None:
		for indice in indices:
			bdp.supprimer(ids[indice])
		if len(indices) > 0:
			update_liste(liste)



# Charger les personnes depuis un fichier sauvegarde auparavant
def charger_personnes(nom_bdp, liste):
	global bdp, ids
	try:
		bdp = BaseDePersonnes.charger(nom_bdp)
		update_liste(liste)
	except BaseDeDonneeInexistanteErreur:
		popup_erreur(liste, "Nom de base de donnees invalide")

# Sauve la bdd de persones dans un fichier
def sauver_personnes(nom_bdp):
	global bdp
	if bdp is not None:
		bdp.nom = nom_bdp
		bdp.sauver()
		
# Cree le popup pour ajouter une personne.
def popup_ajouter(liste, prenom="", nom="", age="", homme="Homme", 
				  nationalite="", metier=""):
	global root, bdp, ids
	popup = Toplevel(root)  # Popup contenant les widgets
	popup.title("Ajouter")
	if bdp is None:
		bdp = BaseDePersonnes("")  # Cree la base si elle n'existait pas
	
	prenom_var = StringVar(value=prenom)
	nom_var = StringVar(value=nom)
	age_var = StringVar(value=age)
	homme_var = StringVar(value=homme)
	nationalite_var = StringVar(value=nationalite)
	metier_var = StringVar(value=metier)
	
	column=0
	row = 0
	entry_avec_label(popup, "Prenom", prenom_var, column, row)
	row += 1
	entry_avec_label(popup, "Nom", nom_var, column, row)
	row += 1
	entry_avec_label(popup, "Age", age_var, column, row)
	row += 1
	creer_radios(popup, ["Homme", "Femme"], homme_var, column, row)
	row += 1
	entry_avec_label(popup, "Nationalite", nationalite_var, column, row)
	row += 1
	entry_avec_label(popup, "Metier", metier_var, column, row)
	row += 1
	
	frame = ttk.Frame(popup)
	ttk.Button(frame, text="OK", 
			   command=
			     lambda:
					 ajouter_personne(liste, prenom_var.get(), nom_var.get(),
					                  age_var.get(), homme_var.get()=="Homme",
					                  nationalite_var.get(), metier_var.get()))\
					   .grid(row=0, column=0)
	ttk.Button(frame, text="Annuler", command=popup.destroy).grid(row=0, column=1)
	frame.grid(row=row, column=0)
	popup.transient(root)

# Affiche la carte d'identite s'il y en a une et un popup d'erreur sinon
def afficher_cis(selection):
	global bdp, ids, root
	for i in selection:
		id = ids[i]
		try:
			bdp.recuperer(id).afficherCarteIdentite()
		except PasDeCarteIdentiteErreur:
			popup_erreur(root, "Pas de carte d'identite pour cette personne")
		
listbox = Listbox(root, width = 50, selectmode="multiple")

ajouter = ttk.Button(root, text='Ajouter', 
					 command=lambda: popup_ajouter(listbox))
				     
suppr = ttk.Button(root, text='Supprimer',
		           command=
				     lambda: supprimer_personnes(listbox, listbox.curselection()))

montrer_ci = ttk.Button(root, text="Montrer CI",
						command=lambda: afficher_cis(listbox.curselection()))

nom_bdp = StringVar()
charger = ttk.Button(root, text='Charger',
					 command=
					   lambda: charger_personnes(nom_bdp.get(), listbox))
					   
sauver = ttk.Button(root, text='Sauvegarder',
					command=
					  lambda: sauver_personnes(nom_bdp.get()))
					  
entry = ttk.Entry(root, textvariable=nom_bdp, width=10)

root.grid_rowconfigure(index=1, weight=1)
root.grid_columnconfigure(index=0, weight=1)
root.grid_columnconfigure(index=1, weight=1)
root.grid_columnconfigure(index=2, weight=1)
root.grid_columnconfigure(index=3, weight=1)
root.grid_columnconfigure(index=4, weight=1)
root.grid_columnconfigure(index=5, weight=1)

listbox.grid(row=1, column=0, columnspan=6, sticky='nswe')
entry.grid(row=0, column=0, columnspan=2, sticky='ew')
charger.grid(row=0, column=2, columnspan=2, sticky='ew')
sauver.grid(row=0, column=4, columnspan=2, sticky='ew')

ajouter.grid(row=2, column=0, columnspan=2, sticky='ew')
suppr.grid(row=2, column=2, columnspan=2, sticky='ew')
montrer_ci.grid(row=2, column=4, columnspan=2, sticky='ew')
root.mainloop()
