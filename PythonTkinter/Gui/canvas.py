from textwrap import fill
from tkinter import *

root= Tk()
canvas_width = 800
canvas_height = 400

root.title('Paint Area')

# root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root,bg='white' ,width=canvas_width, height=canvas_height)
can_widget.pack()

# x1,y1 x2 y2
can_widget.create_line(0,200,800,200,fill='blue')
can_widget.create_line(400,0,400,400)

can_widget.create_rectangle(20,20,380,180,fill='red')

can_widget.create_oval(420,20,780,180,fill='blue')

can_widget.create_oval(120,220,280,380,fill='yellow')

can_widget.create_arc(500, 250, 700,
                   350, start=0,
                   extent=359,
                   fill="black")

photo = PhotoImage(file='0.png')
can_widget.create_image(388,183,image=photo, anchor= 'nw')


root.mainloop()