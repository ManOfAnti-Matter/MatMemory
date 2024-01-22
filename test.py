from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Hello World")
frm = ttk.Frame(root, padding=100)
frm.grid(row=0, column=0, sticky="nwes")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frm.grid()
lbl = ttk.Label(frm, text="Hello World!")
lbl.grid(column=0, row=0, sticky="e")
btn = ttk.Button(frm, text="Quit", default="disabled", command=root.destroy)
btn.grid(column=1, row=0, sticky="w")
frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.rowconfigure(0, weight=1)

btn.bind("<Return>", lambda e: btn.invoke())

print(btn.config().keys())
print(help(root.geometry))

root.mainloop()
