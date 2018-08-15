from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popoup', message='Button pressed')

window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()

