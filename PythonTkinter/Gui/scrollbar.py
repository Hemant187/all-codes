from logging import root
from tkinter import *
 
root =  Tk()
root.geometry("443x350")
root.title("ScrollBar")

str ="""

pygame documentation
Pygame Home || Help Contents || Reference Index
 
Most useful stuff: Color | display | draw | event | font | image | key | locals | mixer | mouse | Rect | Surface | time | music | pygame

Advanced stuff: cursors | joystick | mask | sprite | transform | BufferProxy
 | freetype | gfxdraw | midi | PixelArray | pixelcopy | sndarray | surfarray | math

Other: camera | controller | examples | fastevent 




Edit on GitHub
Navigation



index
modules |
next |
previous |
pygame v2.1.1 documentation »
pygame.cdrom
© Copyright 2000-2021, pygame developers."""
scrollbar =  Scrollbar(root)
scrollbar.pack(side='right',fill='y')

# listbox = Listbox(root,yscrollcommand=scrollbar.set)
# listbox.pack()
# for i in range(301):
#     listbox.insert(END,f"{i}")

text = Text(root, yscrollcommand=scrollbar.set)
text.pack()

# scrollbar.config(command =listbox.yview)
scrollbar.config(command =text.yview)
text.insert(END, str)



root.mainloop()