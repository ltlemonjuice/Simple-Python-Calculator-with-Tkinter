#Tkinter Test Project: Calculator
from Tkinter import *


class App:

    def __init__(self, master):

        UI = Frame(master)
        Out = Frame(master)
        UI.pack()
        Out.pack()

        resultBox = Message(Out, text="Test Message", width=100)
        resultBox.pack(side=TOP)

        self.button = Button(UI, text="QUIT", fg="red", command=UI.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(UI, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
