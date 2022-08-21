from tkinter import *

class GUI(Tk):
    def __init__(self) :
        super().__init__()
        self.geometry("443x350")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusval = Label(self,textvariable=self.var,relief=SUNKEN,anchor='w')
        self.statusval.pack(side=BOTTOM, fill='x')

    def listbox(self,strinput):
        lbx = Listbox(self)
        lbx.pack()
        lbx.insert(END, strinput)
        
    def click(self):
        print('clicked')

    def checkbutton(self,inttext):
        Button(text=inttext,command=self.click).pack()

if __name__ == "__main__":
    window = GUI()
    window.status() 
    window.listbox('hello world')
    window.checkbutton('click me')
    window.mainloop()
