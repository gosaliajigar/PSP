import os
from Symbol import Symbol
from yahoo_finance import Share
from library import *
from constants import *

"""

Program : psp.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 - Python Programming
Prof.   : Srinivasan Mandyam

Personal Stock Portfolio is a Terminal Based UI software that loads list of stock symbols and gives user capability to ...
	1. View Stock Symbols
	2. Get Stock Symbols latest information
	3. Add Stock Symbol to user's list
	4. Delete Stock Symbol from user's list
	5. Refresh Stock Symbol/Symbols information

Personal Stock Portfolio needs internet connection so that Yahoo! Finance module can retrieve latest information about Stock Symbol.

"""

def init():
    """ init takes care of following ...
        1. Creates default admin login account
        2. Creates logs directory for dumping logs
        3. Downloads symbols, if couldn't download then uses back-up symbols. """
    adminCreation()
    logsDirectory()
    downloadSymbols()

def main():
    """ main loads symbols from downloaded files or backup files, displays the welcome screen and waits for
        user to input command.

        main handles input command and upon exit displays end credits. """
    logout = False
    # Symbol Files
    symbolFiles = [NASDAQ_FILE, OTHERS_FILE]
    # Load Symbols from downloaded files
    symbolDictionary = loadSymbols(symbolFiles)
    # If there was an error in downloading files, load symbols from back-up files
    if len(symbolDictionary) <= BACKUP_SYMBOLS_COUNT:
        symbolFiles = [BACKUP_NASDAQ_FILE, BACKUP_OTHERS_FILE]
        symbolDictionary = loadSymbols(symbolFiles)
    # Sort symbols 
    sortedSymbols = sorted(symbolDictionary)
    # Total no. of symbols loaded
    totalNoOfSymbols = len(sortedSymbols)

    # Main Loop
    while (not logout):
        mainMenu = True;
        while (not logout or mainMenu):
            print(NEWLINE * 50)
            # Display Main Menu along with information about symbols loaded
            displayMainMenu(symbolFiles, totalNoOfSymbols)
            # User Input Command
            command = input(COMMAND_CONTINUE)
            # Handle Sign In command
            if signIn(command):
                if not login(USER_DATABASE_DIRECTORY, sortedSymbols, symbolDictionary, totalNoOfSymbols):
                    input(ENTER_GO_BACK_AND_TRY_AGAIN)
                mainMenu = True
                logout = False
            # Handle Sign Up command
            elif signUp(command):
                # Create User
                if createUser(USER_DATABASE_DIRECTORY):
                    input(ENTER_GO_BACK_AND_LOGIN)
                else:
                    input(ENTER_GO_BACK_AND_TRY_AGAIN)
            # Handle Forgot Password command
            elif forgot(command):
                # Reset Password
                if resetPassword(USER_DATABASE_DIRECTORY):
                    input(ENTER_GO_BACK_AND_LOGIN)
                else:
                    input(ENTER_GO_BACK_AND_TRY_AGAIN)
            # Handle About command
            elif about(command):
                displayAbout()
                input(ENTER_GO_BACK)
            # Handle Commands command
            elif commands(command):
                displayCommands()
                input(ENTER_GO_BACK)
            # Handle Log out command
            elif logOut(command):
                mainMenu = False
                logout = True
                break
    # End Credits
    endCredits()

"""
    Starting Point of Stock Portfolio Software
"""
init()
main()

