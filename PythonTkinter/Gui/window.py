from tkinter import *


def resize_win():
    root_width = widthvalue.get()
    root_height = heightvalue.get()
    root.geometry(f"{root_width}x{root_height}")


root = Tk()

root_width = 443
root_height = 350
root.geometry(f"{root_width}x{root_height}")
root.title("Gui Window")

Label(text='width').grid(row=0, column=1)
Label(text='height').grid(row=1, column=1)

widthvalue = StringVar()
widthvar = Entry(root, textvariable=widthvalue)
widthvar.grid(row=0, column=2)

heightvalue = StringVar()
heightvar = Entry(root, textvariable=heightvalue)
heightvar.grid(row=1, column=2)

Button(root, text='Submit', command=resize_win).grid(row=2, column=2)

root.mainloop()
