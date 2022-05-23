# This program will pick lucky lotto numbers for you.
from tkinter import *
from random import randint
window = Tk()
# Widgets:
image = PhotoImage(file = "lotto.gif")
imglabel = Label(window, image=image)
num1 = Label(window, relief="groove", width=2)
num2 = Label(window, relief="groove", width=2)
num3 = Label(window, relief="groove", width=2)
num4 = Label(window, relief="groove", width=2)
num5 = Label(window, relief="groove", width=2)
num6 = Label(window, relief="groove", width=2)
getbtn = Button(window)
resbtn = Button(window)
# Geometry:
imglabel.grid(row=1, column=1, rowspan=2)
num1.grid(row=1, column=2, padx=10)
num2.grid(row=1, column=3, padx=10)
num3.grid(row=1, column=4, padx=10)
num4.grid(row=1, column=5, padx=10)
num5.grid(row=1, column=6, padx=10)
num6.grid(row=1, column=7, padx=(10,20))
getbtn.grid(row=2, column=2, columnspan=4)
resbtn.grid(row=2, column=6, columnspan=2)
# Static Properties:
window.title("Lotto Number Picker")
window.resizable(0, 0)
getbtn.configure(text="Get My Lucky Numbers...")
resbtn.configure(text="Reset")
# Initial Properties:
num1.configure(text="...")
num2.configure(text="...")
num3.configure(text="...")
num4.configure(text="...")
num5.configure(text="...")
num6.configure(text="...")
resbtn.configure(state=DISABLED)
# Dynamic properties:
def pick():
    r1 = randint(1,49)
    r2 = randint(1,49)
    r3 = randint(1,49)
    r4 = randint(1,49)
    r5 = randint(1,49)
    r6 = randint(1,49)
    num1.configure(text=r1)
    num2.configure(text=r2)
    num3.configure(text=r3)
    num4.configure(text=r4)
    num5.configure(text=r5)
    num6.configure(text=r6)
    getbtn.configure(state=DISABLED)
    resbtn.configure(state=NORMAL)
def reset():
    num1.configure(text="...")
    num2.configure(text="...")
    num3.configure(text="...")
    num4.configure(text="...")
    num5.configure(text="...")
    num6.configure(text="...")
    getbtn.configure(state=NORMAL)
    resbtn.configure(state=DISABLED)
getbtn.configure(command=pick)
resbtn.configure(command=reset)
# Sustain Window:
window.mainloop()
