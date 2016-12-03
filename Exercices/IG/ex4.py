from tkinter import Tk, StringVar
import tkinter.ttk as ttk

def update_label(label, var):
    """
    Met a jour le texte de label en fonction de var.
    """
    text = var.get()
    label["foreground"] = text
    label["text"] = text


root = Tk()
choice = ['red', 'green', 'blue']
color = StringVar(root, 'red')
labelX = ttk.Label(root, anchor="center", width=30)
update_label(labelX, color)

i = 1
for value in choice:
    radiobutton = ttk.Radiobutton(root, text=value, variable=color, value=value,
                              command=lambda: update_label(labelX, color), width=30)

    radiobutton.grid(row=i, column=0)
    i += 1

labelX.grid(row=0, column=0, columnspan=3)
root.mainloop()
