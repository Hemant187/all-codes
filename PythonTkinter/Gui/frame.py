from tkinter import * 

root = Tk()
root.geometry("600x300")

f1 = Frame(root,bg='grey',borderwidth=5,relief=RAISED)
f1.pack()

l1 = Label(f1,text="Welcome to frames")
l1.pack(pady=50)

f2 = Frame(root,bg='blue',borderwidth = 8,background='black',relief=SUNKEN)
f2.pack(side='bottom',fill='y')
l2 = Label(f2,text="Hello World")
l2.pack()
root.mainloop()