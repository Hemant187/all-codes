from tkinter import *


root = Tk()
root.geometry("400x363")
root.title("My GUI With Harry")


"""Important Label Options
text = add the text
bg = background
fg = foreground
font = sets the font
 1. font=('comicsansns',19,'bold')
 2. font=('comicsansns 19 bold')
padx = x padding
pady = y padding
relief border styling = SUNKEN , RAISED ,GROOVE , RIDGE
"""


title_label =Label(text="Hello I am Hemant from India.",padx=200,pady=200,bg='red',fg='yellow',
font=('comicsansns 19 bold'),borderwidth="2", relief=SUNKEN)
"""Important pack options
anchor = nw
side = bottom,top,left,right
fill
padx
pady
"""
title_label.pack(side='left',fill=Y,padx=20,pady=30)

root.mainloop()
