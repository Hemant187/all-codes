from tkinter import *
import tkinter.messagebox as tmsg

def myorder():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")
root = Tk()
root.geometry("445x350")

Label(text="What would you like to order ?",font='lucida 19 bold').pack()

var = StringVar()
# var = IntVar()
var.set('Radio')

food =['Dosa','Italy','Pav','Somosa']
# count = 0
# var.set(count)
for i in food:
    
    radio = Radiobutton(root,text=f'{i}',variable=var,value=i,padx=10)
    # count += 1
    radio.pack(anchor='w')
    
    

Button(text="Order",command=myorder,padx=20).pack()
root.mainloop()