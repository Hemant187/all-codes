from tkinter import *
from PIL import Image,ImageTk

def every_100(text):
    final_text = ''
    for i in range(len(text)):
        final_text += text[i]
        if i%100==0 and i!=0:
            final_text += '\n' 
    return final_text


root = Tk()
root.geometry('800x800')


texts = []
photos = []
for i in range(3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    
    image = Image.open(f"{i+1}.png")
    image = image.resize((150,150), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root,width=100,height=70)
Label(f0,text='Apka Apna Akhabar',font='bold 33').pack()
Label(f0,text='15 - August - 2022',font='22').pack()
f0.pack()

for i in range(0,3):
    
    f = Frame(root,width=700,height=100,pady=14)
    Label(f,text=texts[i],anchor='nw',padx=20).pack(side='left')
    Label(f,image=photos[i]).pack()
    f.pack()


root.mainloop()