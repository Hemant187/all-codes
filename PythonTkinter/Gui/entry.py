from tkinter import *

def getvals():
    with open('data/login.txt','a') as file:
        file.writelines([uservalue.get(),'  ' , passvalue.get()])
        


root =  Tk()
root.geometry("433x350")

username =  Label(text="Username",font='bold 10')
password = Label(text="Password",font='bold 10')

username.grid()
password.grid()

# BooleanVar,IntVar,StringVar,DoubleVar
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=uservalue)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(column=1,row=0)
passentry.grid(column=1,row=1)

Button(text="Submit",command=getvals).grid()

root.mainloop()