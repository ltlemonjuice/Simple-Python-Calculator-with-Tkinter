#Tkinter Test Project: Calculator
from Tkinter import *


class App:

    def __init__(self, master):

        UI = Frame(master)
        Out = Frame(master)
        Out.pack()
        UI.pack()

        
        
        buttonHeight = 4
        buttonWidth = 8

        self.setup(UI, Out, buttonHeight, buttonWidth)
        
    def setup(self, UI, Out, buttonHeight, buttonWidth):
        self.resultBox = Label(Out, text="Citric Calculator Initiated...", height=buttonHeight)
        self.resultBox.grid()

        global Shit 
        Shit = ""

        def Output(Stuff):
            self.resultBox.grid_forget()
            self.resultBox = Label(Out, text=Stuff, height=buttonHeight)
            self.resultBox.grid()

        def addInput(text):
            global Shit
            Shit = Shit + str(text)
            Output(Shit)

        def reset():
            global Shit
            Shit = ""
            Output(Shit)

        def evaluate():
            global Shit
            try:
                Result = eval(Shit)
                Output(Result)
            except:
                if (Shit == ""):
                    Output("")
                else:
                    Output("ERROR")
                
                    
        #ROW 0
        self.Clear = Button(UI, text="C", command=lambda: reset(), height=buttonHeight, width=buttonWidth)
        self.Clear.grid(column=0, row=0)

        self.PAROPEN = Button(UI, text="(", command=lambda: addInput("*("), height=buttonHeight, width=buttonWidth)
        self.PAROPEN.grid(column=1, row=0)

        self.PARCLOSE = Button(UI, text=")", command=lambda: addInput(")"), height=buttonHeight, width=buttonWidth)
        self.PARCLOSE.grid(column=2, row=0)

        self.DIVIDE = Button(UI, text="/", command=lambda: addInput("/"), height=buttonHeight, width=buttonWidth)
        self.DIVIDE.grid(column=3, row=0)

        #ROW 1
        self.SEVEN = Button(UI, text="7", command=lambda: addInput("7"), height=buttonHeight, width=buttonWidth)
        self.SEVEN.grid(column=0, row=1)

        self.EIGHT = Button(UI, text="8", command=lambda: addInput("8"), height=buttonHeight, width=buttonWidth)
        self.EIGHT.grid(column=1, row=1)

        self.NINE = Button(UI, text="9", command=lambda: addInput("9"), height=buttonHeight, width=buttonWidth)
        self.NINE.grid(column=2, row=1)

        self.MULTI = Button(UI, text="*", command=lambda: addInput("*"), height=buttonHeight, width=buttonWidth)
        self.MULTI.grid(column=3, row=1)

        #ROW 2
        self.FOUR = Button(UI, text="4", command=lambda: addInput("4"), height=buttonHeight, width=buttonWidth)
        self.FOUR.grid(column=0, row=2)

        self.FIVE = Button(UI, text="5", command=lambda: addInput("5"), height=buttonHeight, width=buttonWidth)
        self.FIVE.grid(column=1, row=2)

        self.SIX = Button(UI, text="6", command=lambda: addInput("6"), height=buttonHeight, width=buttonWidth)
        self.SIX.grid(column=2, row=2)

        self.MINUS = Button(UI, text="-", command=lambda: addInput("-"), height=buttonHeight, width=buttonWidth)
        self.MINUS.grid(column=3, row=2, rowspan=1)

        #ROW 3
        self.ONE = Button(UI, text="1", command=lambda: addInput("1"), height=buttonHeight, width=buttonWidth)
        self.ONE.grid(column=0, row=3)

        self.TWO = Button(UI, text="2", command=lambda: addInput("2"), height=buttonHeight, width=buttonWidth)
        self.TWO.grid(column=1, row=3)

        self.THREE = Button(UI, text="3", command=lambda: addInput("3"), height=buttonHeight, width=buttonWidth)
        self.THREE.grid(column=2, row=3)

        self.PLUS = Button(UI, text="+", command=lambda: addInput("+"), height=buttonHeight, width=buttonWidth)
        self.PLUS.grid(column=3, row=3, rowspan=1)

        #ROW 4
        self.ZERO = Button(UI, text="0", command=lambda: addInput("0"), height=buttonHeight, width=buttonWidth)
        self.ZERO.grid(column=0, row=4)

        self.DOT = Button(UI, text=".", command=lambda: addInput("."), height=buttonHeight, width=buttonWidth)
        self.DOT.grid(column=1, row=4)

        self.POW = Button(UI, text="", command=lambda: Output("SURPRIIIIISE!!"), height=buttonHeight, width=buttonWidth)
        self.POW.grid(column=2, row=4)

        self.ENTER = Button(UI, text="ENTER", command=lambda: evaluate(), height=buttonHeight, width=buttonWidth)
        self.ENTER.grid(column=3, row=4, columnspan=1)

       

    

root = Tk()

app = App(root)

root.mainloop()
