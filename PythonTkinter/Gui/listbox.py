from tkinter import *

root = Tk()
root.geometry("443x350")
root.title('Listbox')

def add_more():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1
i = 0
lbx =  Listbox(root)
lbx.pack()
lbx.insert(END,'How are you?')

Button(text='add more',command=add_more).pack()

root.mainloop()