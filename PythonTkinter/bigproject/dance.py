from tkinter import *
from csv import writer


def algo():
    with open(r'C:\Users\hksai\OneDrive\Desktop\my codes\PythonTkinter\data\dance.txt', 'a') as file:
        file.write(
            f"Name = {namevalue.get()},Contact = {contactvalue.get()},Location = {locationvalue.get()} \n")
    with open(r'C:\Users\hksai\OneDrive\Desktop\my codes\PythonTkinter\data\dance.csv', 'a') as file:
        obj = writer(file)
        obj.writerow(
            [namevalue.get(), contactvalue.get(), locationvalue.get()])


root = Tk()
root.geometry("443x333")

Label(text="The Dance Class", fg='yellow', bg='black',
      font='bold 20',).grid(row=0, column=1)

name = Label(text='Name', font='bold 10')
contact = Label(text='Contact', font='bold 10')
location = Label(text='Location', font='bold 10')

name.grid()
contact.grid()
location.grid()

namevalue = StringVar()
contactvalue = StringVar()
locationvalue = StringVar()

namevar = Entry(root, textvariable=namevalue)
contactvar = Entry(root, textvariable=contactvalue)
locationvar = Entry(root, textvariable=locationvalue)

namevar.grid(row=1, column=1)
contactvar.grid(column=1, row=2)
locationvar.grid(column=1, row=3)

Button(text='Submit', command=algo).grid(column=2, row=2)

root.mainloop()
