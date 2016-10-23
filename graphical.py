from tkinter import *


class GraphicalPSP(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Graphical PSP")
        self.master.geometry("1500x900")

        self._emptyLabel = Label(self, text = "")
        self._emptyLabel.grid(row = 0, rowspan = 8, column = 1, columnspan = 20)

        self._userNameLabel = Label(self, text = "User Name")
        self._userNameLabel.grid(row = 10, column = 10, columnspan = 2)
        self._userNameVar = StringVar()
        self._userNameEntry = Entry(self, textvariable = self._userNameVar)
        self._userNameEntry.grid(row = 10, column = 12, columnspan = 2)

        self._passwordLabel = Label(self, text = "Password")
        self._passwordLabel.grid(row = 11, column = 10, columnspan = 2)
        self._passwordVar = StringVar()
        self._passwordEntry = Entry(self, textvariable = self._passwordVar)
        self._passwordEntry.grid(row = 11, column = 12, columnspan = 2)

        self._signInButton = Button(self, text = "Sign In")
        self._signInButton.grid(row = 12, column = 10, columnspan = 2)

        self._signUpButton = Button(self, text = "Sign Up")
        self._signUpButton.grid(row = 12, column = 12, columnspan = 4)

        self.grid()

def main():
    GraphicalPSP().mainloop()

main()
