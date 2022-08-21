from tkinter import *

root = Tk()
root.geometry("500x4000")

lb = Label(text="Harry Newspaper \nDate=12-08-2022",font="bold 21",bg='black',fg='white')
lb.pack()

photo = PhotoImage(file =r'./sprites/1.png')
im1 = Label(image = photo)
im1.pack()

with open(r'C:\Users\hksai\OneDrive\Desktop\my codes\PythonTkinter\data\news.txt','r') as file:
    obj = file.read()
    Label(text=obj).pack()
root.mainloop()