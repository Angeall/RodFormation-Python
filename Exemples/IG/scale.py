from tkinter import IntVar, Tk, Entry
import tkinter.ttk as ttk

root = Tk()
value = IntVar(root)
scale = ttk.Scale(root, from_=0, to=16, 
                 variable=value, 
                 orient='v')
entry = Entry(root, textvariable=value)

scale.grid(row=0, column=0)
entry.grid(row=0, column=1)

root.mainloop()
