#Tkinter Test Project: Calculator
from Tkinter import *


class App:

    def __init__(self, master):

        UI = Frame(master)
        Out = Frame(master)
        Out.pack()
        UI.pack()

        Input = ""
        
        buttonHeight = 4
        buttonWidth = 8

        self.setup(UI, Out, buttonHeight, buttonWidth)
        
    def setup(self, UI, Out, buttonHeight, buttonWidth):
        self.resultBox = Label(Out, text="Citric Calculator Initiated...", height=buttonHeight)
        self.resultBox.grid()

        def hello():
            print("Hello")
            
        #ROW 0
        self.Pi = Button(UI, text="Pi", command=hello(), height=buttonHeight, width=buttonWidth)
        self.Pi.grid(column=0, row=0)

        self.PAROPEN = Button(UI, text="(", command=None, height=buttonHeight, width=buttonWidth)
        self.PAROPEN.grid(column=1, row=0)

        self.PARCLOSE = Button(UI, text=")", command=None, height=buttonHeight, width=buttonWidth)
        self.PARCLOSE.grid(column=2, row=0)

        self.DIVIDE = Button(UI, text="/", command=None, height=buttonHeight, width=buttonWidth)
        self.DIVIDE.grid(column=3, row=0)

        #ROW 1
        self.SEVEN = Button(UI, text="7", command=None, height=buttonHeight, width=buttonWidth)
        self.SEVEN.grid(column=0, row=1)

        self.EIGHT = Button(UI, text="8", command=None, height=buttonHeight, width=buttonWidth)
        self.EIGHT.grid(column=1, row=1)

        self.NINE = Button(UI, text="9", command=None, height=buttonHeight, width=buttonWidth)
        self.NINE.grid(column=2, row=1)

        self.MULTI = Button(UI, text="*", command=None, height=buttonHeight, width=buttonWidth)
        self.MULTI.grid(column=3, row=1)

        #ROW 2
        self.FOUR = Button(UI, text="4", command=None, height=buttonHeight, width=buttonWidth)
        self.FOUR.grid(column=0, row=2)

        self.FIVE = Button(UI, text="5", command=None, height=buttonHeight, width=buttonWidth)
        self.FIVE.grid(column=1, row=2)

        self.SIX = Button(UI, text="6", command=None, height=buttonHeight, width=buttonWidth)
        self.SIX.grid(column=2, row=2)

        self.MINUS = Button(UI, text="-", command=None, height=buttonHeight, width=buttonWidth)
        self.MINUS.grid(column=3, row=2, rowspan=1)

        #ROW 3
        self.ONE = Button(UI, text="1", command=None, height=buttonHeight, width=buttonWidth)
        self.ONE.grid(column=0, row=3)

        self.TWO = Button(UI, text="2", command=None, height=buttonHeight, width=buttonWidth)
        self.TWO.grid(column=1, row=3)

        self.THREE = Button(UI, text="3", command=None, height=buttonHeight, width=buttonWidth)
        self.THREE.grid(column=2, row=3)

        self.PLUS = Button(UI, text="+", command=None, height=buttonHeight, width=buttonWidth)
        self.PLUS.grid(column=3, row=3, rowspan=1)

        #ROW 4
        self.ZERO = Button(UI, text="0", command=None, height=buttonHeight, width=buttonWidth)
        self.ZERO.grid(column=0, row=4)

        self.DOT = Button(UI, text=".", command=None, height=buttonHeight, width=buttonWidth)
        self.DOT.grid(column=1, row=4)

        self.POW = Button(UI, text="^", command=None, height=buttonHeight, width=buttonWidth)
        self.POW.grid(column=2, row=4)

        self.ENTER = Button(UI, text="ENTER", command=None, height=buttonHeight, width=buttonWidth)
        self.ENTER.grid(column=3, row=4, columnspan=1)

       

    def Output(self, Stuff, Out, resultBox, buttonHeight):
        self.resultBox.grid_forget()
        self.resultBox = Label(Out, text=Stuff, height=buttonHeight)
        self.resultBox.grid()

    def addInput(self):
        return None

root = Tk()

app = App(root)

root.mainloop()
