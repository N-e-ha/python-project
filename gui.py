import pyqrcode
from tkinter import *
import os


windows = Tk()
windows.configure(background='Lightgoldenrod2')
windows.geometry('1280x720')

folder_path = StringVar()


def clear():
    en1.delete(first=0, last=100)


def create():
    Link=en1.get()
    te = pyqrcode.create(Link)
    te.png('yourqrcode.png')
    os.system('yourqrcode.png')


lb1 = Label(windows, width=20, text='Qr code generator', fg='Black', bg='Lightgoldenrod2',
            font=('times', 30, 'bold'))
lb1.place(x=430, y=50)

lb2 = Label(windows, width=12, height=2, text='Link', fg='Black', bg='goldenrod1', font=('times', 25, 'bold'))
lb2.place(x=150, y=200)

en1 = Entry(windows, width=15, fg='Black', bg='tan1', font=('times', 50, 'italic'))
en1.place(x=450, y=200)

clearbt = Button(windows, width=12, height=2, command=clear, text='Clear', fg='Black', bg='gold',
                 font=('times', 18, 'bold'))
clearbt.place(x=1000, y=200)
down = Button(windows, width=20, height=1, text='Create and show', command=create, fg='Black', bg='orange',
              font=('times', 18, 'bold'))
down.place(x=530, y=450)

bottom = Label(windows, width=120, height=1, text='© Neha and Priyanka', fg='Black', bg='snow', font=('times', 15, 'bold'))
bottom.place(x=00, y=650)


windows.mainloop()
