from tkinter import *
import tkinter.messagebox as tmsx

def myfun():
    print("hello")

def help():
    tmsx.showinfo('help','harry will help you')

def rate():
    value = tmsx.askquestion('rate us','would you like this app')
    if value == 'yes':
        msg = 'Rate us on appstore'
    else:
        msg = 'what should we do'
    tmsx.showinfo('Experience',msg)

def delete():
    ans = tmsx.askretrycancel('anti-virus','do you want to delete antivirus')
    if ans:
        print("Don't do retry bcz you cann't delete anti-virus")
    else:
        print("Good , this is for your safety")


root = Tk()
root.geometry("443x350")

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label='new file',command=myfun)
m1.add_command(label='open file',command=myfun)
m1.add_separator()
m1.add_command(label='new window',command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="file",menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label='copy',command=myfun)
m2.add_command(label='paste',command=myfun)
m2.add_separator()
m2.add_command(label='undo',command=myfun)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label='help',command=help)
m3.add_command(labe="rate us",command=rate)
m3.add_command(labe="delete",command=delete)
root.config(menu=mainmenu)
mainmenu.add_cascade(label='Help',menu=m3)

root.mainloop()