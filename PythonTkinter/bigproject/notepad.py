from tkinter import *
from tkinter.messagebox import showinfo
import os
from tkinter.filedialog import askopenfilename,  asksaveasfilename


def newFile():
    global file
    root.title("Untitled -Notepad")
    file = None
    textarea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ('Text Document', '*.txt')])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, 'r')
        textarea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Document", "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")


def exitFile():
    root.destroy()


def Cut():
    textarea.event_generate("<<Cut>>")


def Copy():
    textarea.event_generate("<<Copy>>")


def Paste():
    textarea.event_generate("<<Paste>>")


def About():
    showinfo("Notepad", "Notepad By Hemant")


root = Tk()
root.geometry("443x350")
root.title("Untitled -Notepad")

Scroll = Scrollbar(root)
Scroll.pack(side=RIGHT, fill=Y)

textarea = Text(root, font='lucida 10', yscrollcommand=Scroll.set)
textarea.pack(expand=True, fill=BOTH)
Scroll.config(command=textarea.yview)

Menubar = Menu(root)
file = None
filebar = Menu(Menubar, tearoff=0)
filebar.add_command(label="New", command=newFile)
filebar.add_command(label="Open", command=openFile)
filebar.add_command(label="Save", command=saveFile)
filebar.add_separator()
filebar.add_command(label="Exit", command=exitFile)
root.config(menu=Menubar)
Menubar.add_cascade(label="File", menu=filebar)

Editbar = Menu(Menubar, tearoff=0)
Editbar.add_command(label="Cut", command=Cut)
Editbar.add_command(label="Copy", command=Copy)
Editbar.add_command(label="Paste", command=Paste)
Menubar.add_cascade(label="Edit", menu=Editbar)

Helpbar = Menu(Menubar, tearoff=0)
Helpbar.add_command(label="About", command=About)
Menubar.add_cascade(label="Help", menu=Helpbar)

root.mainloop()
