from tkinter import *


root = Tk()
root.geometry("200x200")

photo = PhotoImage(file='./sprites/0.png')
lab = Label(image=photo)
lab.pack()

photo1 = PhotoImage(file='./sprites/1.png')
lab1 = Label(image=photo1)
lab1.pack()

photo2 = PhotoImage(file='./sprites/2.png')
lab2 = Label(image=photo2)
lab2.pack()

root.mainloop()

