from tkinter import *

def click(event):
    global starvar
    text  = event.widget.cget("text")
    if text == '=':
        if starvar.get().isdigit():
            Value = int(starvar.get())
        else:
            try:
                Value = eval(screen.get())
            except:
                Value = 'error'
        starvar.set(Value)
        screen.update()
    
    elif text == "C":
        starvar.set("")
        screen.update()

    else:
        starvar.set(starvar.get() + str(text))
        screen.update()

root  = Tk()
root.geometry("450x500")
root.title("Calculator by Hemant")

Label(text="CALCULATOR",font="lucida 30 bold").pack()
starvar = StringVar()
starvar.set("")
screen = Entry(root,textvariable=starvar,font="lucida 40 bold")
screen.pack(fill='x')

f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()
f4 = Frame(root)
f4.pack()

j = [9,8,7,'+',6,5,4,'- ',3,2,1,'* ','=','0','/ ','C']
k = [6,5,4,'-']
l = [3,2,1,' *']
m = ['=',' 0',' /',' C']

f = f1
for i in j:
    if i in k:
        f = f2
    elif i in l:
        f = f3
    elif i in m:
        f = f4
    b =Button(f,text=i,font="lucida 35 bold",padx=15)
    b.pack(side='left')
    b.bind("<Button-1>",click)
    
root.mainloop()