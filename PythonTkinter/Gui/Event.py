from tkinter import *

def harry(event):
    print(f"You clicked on button at {event.x},{event.y}")
root = Tk()
root.geometry("443x350")
root.title("Event Handling")

widget = Button(text="click me")
widget.pack()
widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()