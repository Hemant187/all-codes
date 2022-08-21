from tkinter import *

root = Tk()
root.geometry("443x350")
root.title("Footer")

def footer():
    import time
    footvar.set('busy...')
    footval.update()
    time.sleep(2)
    footvar.set("Ready")

footvar = StringVar()
footvar.set("Ready")
footval = Label(text='Ready',textvariable=footvar,relief=SUNKEN,anchor='w')
footval.pack(side=BOTTOM,fill='x')

Button(text='Upload',command=footer).pack()

root.mainloop()