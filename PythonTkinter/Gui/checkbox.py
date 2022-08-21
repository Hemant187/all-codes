from tkinter import *

def getvals():
    print('Get it!')
    with open(
        r"C:\Users\hksai\OneDrive\Desktop\my codes\PythonTkinter\data\travel.txt",'a') as file:
        file.write(
            f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get(),checkvalue.get()}\n")


root = Tk()
root.geometry("640x344")

Label(text='Welcome to Harry travels',font='bold 15',pady=15).grid(row=0,column=3)

name = Label(text='Name')
phone = Label(text='Phone')
gender = Label(text='Gender')
emergency = Label(text='Emergency')
paymentmode = Label(text='Paymentmode')

name.grid(column=2 , row=1)
phone.grid(column=2, row=2)
gender.grid(column=2, row=3)
emergency.grid(column=2, row=4)
paymentmode.grid(column=2, row=5)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
checkvalue = IntVar()

namevar = Entry(root, textvariable=namevalue)
phonevar = Entry(root, textvariable=phonevalue)
gendervar = Entry(root, textvariable=gendervalue)
emergencyvar = Entry(root, textvariable=emergencyvalue)
paymentmodevar = Entry(root, textvariable=paymentmodevalue)

checkbox = Checkbutton(text="Want to prebook your meal?" ,variable=checkvalue)
checkbox.grid(column=3,row=7)

namevar.grid(column=3,row=1)
phonevar.grid(column=3,row=2)
gendervar.grid(column=3,row=3)
emergencyvar.grid(column=3,row=4)
paymentmodevar.grid(column=3,row=5)

Button(text="Submit to Harry travels",command=getvals).grid(column=3,row=8)

root.mainloop()