from tkinter import Tk
import tkinter.ttk as ttk 
racine = Tk() 

style = ttk.Style()
style.configure("MonStyle.TLabel", padding=5,  
				foreground="#FF0000", 
				font=("Helvetica", 12))
style.configure("MonStyle2.TLabel", padding=5, 
				foreground="#0000FF", 
				background="#00FF00")
label = ttk.Label(racine, text="Hello World", 
				  anchor="center")
label2 = ttk.Label(racine, text="Hello World", 
				   style="MonStyle.TLabel")
label3 = ttk.Label(racine, text="Hello World",  
				   style="MonStyle2.TLabel")
label.grid(column=0, row=0, columnspan=2)
label2.grid(column=0, row=1)
label3.grid(column=1, row=1)

racine.mainloop() 
