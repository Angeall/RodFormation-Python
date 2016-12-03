from tkinter import Tk
import tkinter.ttk as ttk
root = Tk()
ttk.Style().configure("A.TFrame", background="#FF0000")
f1 = ttk.Frame(root, style="A.TFrame")
ttk.Label(f1, text='je suis dans F1').grid(row=0, column=0)
ttk.Label(f1, text='moi aussi dans F1').grid(row=0, column=1)
ttk.Label(f1, text='et enfin moi aussi').grid(row=1, column=0)

f1.grid(row=0, column=0)
ttk.Label(root, text='je suis dans root').grid(row=1, column=0)
ttk.Label(root, text='moi aussi dans root').grid(row=2, column=0)

root.mainloop()
