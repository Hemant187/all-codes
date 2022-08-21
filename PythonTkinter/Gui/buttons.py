from tkinter import *

root = Tk()
root.geometry("400x400")

root.minsize(300,200)
root.maxsize(600,600)

def Hello():
    print('Hello')

def I():
    print("I")

def am():
    print("am")

def Hemant():
    return print("Hemant")
frame = Frame(root,borderwidth=3,background='blue' ,bg='yellow')
frame.pack(anchor='n',fill=X)

b1 = Button(frame,text="Hello",command=Hello)
b1.pack(side='left',padx=20)

b2 = Button(frame,text="  I  ",command=I)
b2.pack(side='left',padx=20)

b3 = Button(frame,text="  am  ",command=am)
b3.pack(side='left',padx=20)

b4 = Button(frame,text="Hemant",command=Hemant)
b4.pack(side='left',padx=20)

root.mainloop()