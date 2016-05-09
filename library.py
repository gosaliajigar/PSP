"""

Program : library.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 - Python Programming
Prof.   : Srinivasan Mandyam

library that would hold all the useful libraries for Stock Portfolio Project.

"""

# For file related operations
import os
# For downloading Stock Symbols files
import urllib.request
# For Yahoo! Finance APIs
from yahoo_finance import Share
# For unique log file names
from datetime import datetime
# PSP : Symbol Object
from Symbol import Symbol
# PSP Constants
from constants import *

# -----------------------
# Pre-Run Setup functions
# -----------------------
def adminCreation():
    """ adminCreation creates admin account on start-up as a pre-setup step. """
    validPasswordFile = False
    validPinFile = False
    while ((not validPasswordFile) or (not validPinFile)):
        if os.path.exists(USER_DATABASE_DIRECTORY):
            if os.path.exists(ADMIN_DIRECTORY):
                if os.path.exists(ADMIN_PASSWORD_FILE):
                    file = open(ADMIN_PASSWORD_FILE, 'r')
                    password = file.read()
                    file.close()
                    if (password != encrypt(ADMIN_PASSWORD)):
                        os.remove(ADMIN_PASSWORD_FILE)
                        file = open(ADMIN_PASSWORD_FILE, 'w')
                        file.write(encrypt(ADMIN_PASSWORD))
                        file.close()
                    validPasswordFile = True
                else:
                    file = open(ADMIN_PASSWORD_FILE, 'w')
                    file.write(encrypt(ADMIN_PASSWORD))
                    file.close()
                if os.path.exists(ADMIN_PIN_FILE):
                    file = open(ADMIN_PIN_FILE, 'r')
                    pin = file.read()
                    file.close()
                    if (pin != encrypt(ADMIN_PIN)):
                        os.remove(ADMIN_PIN_FILE)
                        file = open(ADMIN_PIN_FILE, 'w')
                        file.write(encrypt(ADMIN_PIN))
                        file.close()
                    validPinFile = True
                else:
                    file = open(ADMIN_PIN_FILE, 'w')
                    file.write(encrypt(ADMIN_PIN))
                    file.close()
            else:
                os.mkdir(ADMIN_DIRECTORY)
        else:
            os.mkdir(USER_DATABASE_DIRECTORY)

def logsDirectory():
    """ logsDirectory creates logs directory for dumping logs when there is an error or exception. """
    if not os.path.exists(LOGS_DIRECTORY):
        os.mkdir(LOGS_DIRECTORY)

def downloadSymbols():
    """ downloadSymbols checks if NASDAQ and OTHERS Stock Symbols are present else triggers their downloads. """
    if not os.path.exists(SYMBOLS_DIRECTORY):
        os.mkdir(SYMBOLS_DIRECTORY)
    if not validFile(NASDAQ_FILE):
        downloadFile(NASDAQ_FILE, NASDAQ_URL)
    if not validFile(OTHERS_FILE):
        downloadFile(OTHERS_FILE, OTHERS_URL)

def downloadFile(fileName, url):
    """ downloadSymbols downloads NASDAQ and OTHERS Stock Symbols. """
    try:
        file = open(fileName, 'w')
        with urllib.request.urlopen(url) as response:
           file.write("".join(map(chr, response.read())))
        file.close()
    except Exception as exception:
        dumpLogs("exception", fileName.split(os.sep)[-1] + "-download", ["Exception :" + repr(exception)])

#------------------------
# User Command Validators
#------------------------
def about(command):
    """ Check if command is ABOUT (a | about). """
    return (command.lower() == 'a' or command.lower() == 'about')

def commands(command):
    """ Check if command is to get available Commands (c | commands). """
    return (command.strip().lower() == 'c' or command.strip().lower() == 'commands')

def logOutUser(command):
    """ Check if command is to log out (o | logout). """
    return (command.strip().lower() == "o" or command.strip().lower() == "logout")

def logOut(command):
    """ Check if command is Quit (b | q | x | e). """
    return (command.strip().lower() == "b" or command.strip().lower() == 'back' or \
            command.strip().lower() == 'q' or command.strip().lower() == 'quit' or \
            command.strip().lower() == 'x' or command.strip().lower() == 'exit' or \
            command.strip().lower() == 'e')

def addSymbol(command):
    """ Check if command is to add stock symbol (a | add [SYM/#]). """
    expression = command.strip().lower()
    words = expression.split()
    return (("a " in expression or "add " in expression) and (words[0] == "a" or words[0] == "add") and len(words) == 2)

def deleteSymbol(command, mySymbols):
    """ Check if command is to delete stock symbol (d | delete [SYM/#]). """
    expression = command.strip().lower()
    words = expression.split()
    return (len(mySymbols) > 0 and ("d " in expression or "delete " in expression) and (words[0] == "d" or words[0] == "delete") and len(words) == 2)

def viewSymbol(command):
    """ Check if command is to view stock symbol (v | view [SYM/#]). """
    expression = command.strip().lower()
    words = expression.split()
    return (("v " in expression or "view " in expression) and (words[0] == "v" or words[0] == "view") and len(words) == 2)

def refreshSymbol(command, mySymbols):
    """ Check if command is to refresh stock symbol (r | refresh [SYM/#]). """
    expression = command.strip().lower()
    words = expression.split()
    return (len(mySymbols) > 0 and ("r " in expression or "refresh " in expression) and (words[0] == "r" or words[0] == "refresh") and len(words) == 2)

def refreshAllSymbol(command, mySymbols):
    """ Check if command is to refresh all stock symbols. """
    return (len(mySymbols) > 0 and (command.strip().lower() == "r" or command.strip().lower() == "refresh") and len(command) == 1)

def getAllListings(command):
    """ Check if command is to get all listings (l | list). """
    return (command.strip().lower() == "l" or command.strip().lower() == "list")

def home(command):
    """ Check if command is to go back to home screen (h | home). """
    return (command.strip().lower() == "h" or command.strip().lower() == "home")

def signIn(command):
    """ Check if command is to Sign In (s | signin). """
    return (command.strip().lower() == 's' or command.strip().lower() == 'signin')

def signUp(command):
    """ Check if command is to sign up (u | signup). """
    return (command.lower() == 'u' or command.lower() == 'signup')

def forgot(command):
    """ Check if command is to reset password (f | forgot). """
    return (command.lower() == 'f' or command.lower() == 'forgot')

#-------------
# Data Loaders
#-------------
def loadSymbols(fileNames):
    """ loadSymbols loads Stock Symbols from given files. """
    noOfSymbols = 0
    symbolDictionary = {}
    for fileName in fileNames:
        if validFile(fileName):
            file = open(fileName, 'r')
            lines = file.read()
            for line in lines.split(NEWLINE):
                if (line.count(PIPE) == 7):
                    symbolAttributes = line.split(PIPE)
                    symbol = symbolAttributes[0]
                    if (len(symbol) > 0 and (symbol.upper() == symbol)):
                        symbolDictionary[symbol] = symbolAttributes[1:]
                        noOfSymbols += 1
            file.close()
    if noOfSymbols == 0:
        loadBackUpSymbols()
    return symbolDictionary

def loadBackUpSymbols():
    """ loadBackUpSymbols loads Stock Symbols from back up files. """
    return loadSymbols([BACKUP_NASDAQ_FILE, BACKUP_OTHERS_FILE])

#----------------------
# User Command Handlers
#----------------------
def displayListings(command, sortedSymbols, symbolDictionary, totalNoOfSymbols):
    """ displayListings displays listings when user wants to check all available Stock Symbols. """
    listings = 1
    listingView = True
    while listingView and len(sortedSymbols) > 0:
        print(NEWLINE * 15)
        pageHeader()
        printSymbolHeader()
        for symbol in sortedSymbols:
            if (listings % LISTING_SIZE == 0):
                print(NEWLINE * 1)
                pageFooter(LIST_MENU_LIST, LIST_MENU)
                print(str(listings - 1) + SPACE + OF + SPACE + str(totalNoOfSymbols))
                command = input(COMMAND_SYMBOL_CONTINUE)
                print(NEWLINE * HEADER_LENGTH)
                if logOut(command):
                    listingView = False
                    break
                elif isValidSymbol(command, sortedSymbols):
                    print(NEWLINE * HEADER_LENGTH)
                    printDetailsFromSymbol(command, symbolDictionary, sortedSymbols)
                    print(NEWLINE * HEADER_LENGTH)
                elif isSymbolNumber(command, sortedSymbols):
                    print(NEWLINE * HEADER_LENGTH)
                    printDetailsFromNumber(int(command.strip()), symbolDictionary, sortedSymbols)
                    print(NEWLINE * HEADER_LENGTH)
                printSymbolHeader()
            printSymbolDetailsHeaderOnViewSymbol(listings, symbol, symbolDictionary)
            listings = (listings + 1) % totalNoOfSymbols

def displayAbout():
    """ displayAbout displays information about PSP project. """
    print(NEWLINE * 50)
    noOfLines = 0
    file = open(ABOUT_FILE, 'r')
    pageHeader()
    for line in file:
        if (noOfLines != 0 and noOfLines % 18 == 0):
            print(NEWLINE * 2)
            input(ENTER_CONTINUE)
            print(NEWLINE * 50)
            pageHeader()
        noOfLines += 1
        print(line, end=EMPTY)
    print(NEWLINE * 2)
    file.close()

def displayCommands():
    """ displayCommands displays available commands at that point in time. """
    print(NEWLINE * 50)
    noOfLines = 0
    file = open(COMMANDS_FILE, 'r')
    pageHeader()
    for line in file:
        if (noOfLines != 0 and noOfLines % 20 == 0):
            print(NEWLINE * 2)
            input(ENTER_CONTINUE)
            print(NEWLINE * 10)
        noOfLines += 1
        print(line, end=EMPTY)
    print(NEWLINE * 2)
    file.close()

def startPortfolio(userName, mySymbols, sortedSymbols, symbolDictionary, totalNoOfSymbols):
    """ startPortfolio starts the personal stock portfolio of the user and gives user capability to add, delete,
        list, view and refresh symbols. """
    while True:
        mySortedSymbols = list(sorted(mySymbols))
        displayMySymbols(userName, mySymbols, mySortedSymbols)
        command = input(COMMAND_CONTINUE)
        if addSymbol(command):
            addMySymbol(command, sortedSymbols, mySymbols)
        elif deleteSymbol(command, mySymbols):
            deleteMySymbol(command, mySortedSymbols, mySymbols)
        elif viewSymbol(command):
            viewMySymbol(command, sortedSymbols, symbolDictionary)
        elif refreshAllSymbol(command, mySymbols):
            refreshAllMySymbol(command, mySortedSymbols, mySymbols)
        elif refreshSymbol(command, mySymbols):
            refreshMySymbol(command, mySortedSymbols, mySymbols)
        elif getAllListings(command):
            displayListings(command, sortedSymbols, symbolDictionary, totalNoOfSymbols)
        elif home(command) or logOut(command) or logOutUser(command):
            break

def login(baseDirectory, sortedSymbols, symbolDictionary, totalNoOfSymbols):
    """ login handles login command. """
    status = False
    attempts = 0
    print(NEWLINE * 50)
    pageHeader()
    print(NEWLINE * 10)
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        userName = input("\t\t\t\t\t\tEnter User Name : ")
        print(NEWLINE * 1)
        password = input("\t\t\t\t\t\tEnter Password  : ")
        print(NEWLINE * 1)
        if checkCredentials(userName, password, baseDirectory):
            status = True
            mySymbols = readMySymbols(baseDirectory + os.sep + userName + os.sep + STOCKS_FILE)
            startPortfolio(userName, mySymbols, sortedSymbols, symbolDictionary, totalNoOfSymbols)
            saveMySymbols(userName, mySymbols, baseDirectory + os.sep + userName + os.sep + STOCKS_FILE)
            break
        else:
            print(NEWLINE * 1)
            print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
            print(NEWLINE * 1)
    return status

def printDetailsFromSymbol(symbol, symbolDictionary, sortedSymbols):
    """ printDetailsFromSymbol prints Symbol details given symbol name. """
    symbolObj = viewSymbolDetails("v " + symbol, sortedSymbols)
    description = symbolDictionary.get(symbol.upper())[0];
    if len(description) > 80:
        description = description[:80]
    header = ("%5d | %-10s | %-80s" % (sortedSymbols.index(symbol.upper()), symbol.upper().center(10), description))
    print(header.center(120), end=EMPTY)
    print(HYPHEN * (len(header) - 1))
    displaySymbol(symbolObj, symbolDictionary)

def printDetailsFromNumber(index, symbolDictionary, sortedSymbols):
    """ printDetailsFromNumber prints Symbol details given index number of symbol in list. """
    symbol = sortedSymbols[index - 1]
    symbolObj = viewSymbolDetails("v " + symbol, sortedSymbols)
    description = symbolDictionary.get(symbol)[0]
    if len(description) > 80:
        description = description[:80]
    header = ("%5d | %-10s | %-80s" % (index, symbol.center(10), description))
    print(header.center(120), end=EMPTY)
    print(HYPHEN * (len(header) - 1))
    displaySymbol(symbolObj, symbolDictionary)

def addMySymbol(command, sortedSymbols, mySymbols):
    """ addMySymbol handles add symbol command. """
    expression = command.strip().lower()
    words = expression.split()
    if (words[1].isdigit() and (int(words[1]) <= (len(sortedSymbols) - 1))):
        symbol = sortedSymbols[int(words[1]) - 1].upper()
        mySymbols[symbol] = getSymbol(symbol)
    elif (words[1].isalpha() and words[1].upper() in sortedSymbols):
        symbol = words[1].upper()
        mySymbols[symbol] = getSymbol(symbol)
    # Special handling when there are no pre-loaded symbols
    elif (words[1].isalpha() and len(sortedSymbols) == 0):
        symbol = words[1].upper()
        mySymbols[symbol] = getSymbol(symbol)

def deleteMySymbol(command, mySortedSymbols, mySymbols):
    """ deleteMySymbol handles delete symbol command. """
    expression = command.strip().lower()
    words = expression.split()
    if (words[1].isdigit() and (int(words[1]) <= (len(mySortedSymbols)))):
        symbol = mySortedSymbols[int(words[1]) - 1].upper()
        mySymbols.pop(symbol, None)
    elif (words[1].isalpha() and words[1].upper() in mySortedSymbols):
        symbol = words[1].upper()
        mySymbols.pop(symbol, None)

def viewMySymbol(command, sortedSymbols, symbolDictionary):
    """ viewMySymbol handles view my symbol command. """
    description = INFO_UNAVAILABLE
    symbolObj = viewSymbolDetails(command, sortedSymbols)
    if (symbolObj != None):
        print(NEWLINE * HEADER_LENGTH)
        if (len(symbolDictionary) > 0 and symbolDictionary.get(symbolObj.getName()) != None):
            description = symbolDictionary.get(symbolObj.getName())[0];
        if len(description) > 80:
            description = description[:80]
        print((symbolObj.getName() + SPACE + PIPE + SPACE + description).center(110))
        displaySymbol(symbolObj, symbolDictionary)

def viewSymbolDetails(command, sortedSymbols):
    """ viewSymbolDetails handles view symbol command which gives detailed information about the Stock Symbol. """
    expression = command.strip().lower()
    words = expression.split()
    if (words[1].isdigit() and (int(words[1]) <= (len(sortedSymbols)))):
        symbol = sortedSymbols[int(words[1]) - 1].upper()
        symbolDetails = getSymbolDetails(symbol)
    elif (words[1].isalpha() and words[1].upper() in sortedSymbols):
        symbol = words[1].upper()
        symbolDetails = getSymbolDetails(symbol)
    # Special handling when there are no pre-loaded symbols
    elif (words[1].isalpha() and len(sortedSymbols) == 0):
        symbol = words[1].upper()
        symbolDetails = getSymbolDetails(symbol)
    else:
        symbolDetails = getSymbolDetails("UNKNOWN")
    return symbolDetails

def refreshMySymbol(command, mySortedSymbols, mySymbols):
    """ refreshMySymbol handles refresh my symbol command. """
    addMySymbol(command, mySortedSymbols, mySymbols)

def refreshAllMySymbol(command, mySortedSymbols, mySymbols):
    """ refreshAllMySymbol handles refresh all my symbols command. """
    for symbol in mySymbols:
        addMySymbol(command + SPACE + symbol, mySortedSymbols, mySymbols)

#------------------
# Decorator Methods
#------------------
def displayMainMenu(fileNames, totalNoOfSymbols):
    """ displayMainMenu displays main menu for the user. """
    pageHeader()
    displayWelcome(fileNames, totalNoOfSymbols)
    pageFooter(MAIN_MENU_LIST, MAIN_MENU)

def displayUserMenu():
    """ displayUserMenu displays User Menu on user's dashboard. """
    print(NEWLINE * 15)
    pageHeader()
    pageFooter(USER_MENU_LIST, USER_MENU)

def pageHeader():
    """ pageHeader displays every page's header. """
    print(NEWLINE * 1)
    print(WELCOME_HEADER.center(LINE_WIDTH), end=EMPTY);
    print((HYPHEN * (len(WELCOME_HEADER) - 1)).center(LINE_WIDTH), end=EMPTY)
    print(NEWLINE * 1)

def welcomeUser(userName):
    """ welcomeUser displays welcome message for the user. """
    print(("!!Welcome " + userName.upper() + "!!").center(LINE_WIDTH), end=EMPTY)
    print((HYPHEN * len("!!Welcome " + userName.upper() + "!!")).center(LINE_WIDTH))

def pageFooter(orderedList, dictionary):
    """ pageFooter displays every page footer with the available commands for each screen. """
    commandDetails = EMPTY
    commands = 0
    for command in orderedList:
        commands += 1
        commandDetails = commandDetails + SPACE + dictionary.get(command, None) + EQUAL + command
        if (commands != (len(dictionary))):
            commandDetails = commandDetails + SPACE + PIPE
    print(commandDetails.center(LINE_WIDTH), end=EMPTY)
    print((HYPHEN * (len(commandDetails) - 1)).center(LINE_WIDTH), end="\n\n")

def endCredits():
    """ endCredits displays end credits when user logs out of PSP. """
    print(NEWLINE * 10)
    print(THANK_YOU_HEADER.center(LINE_WIDTH), end=EMPTY);
    print((HYPHEN * (len(THANK_YOU_HEADER) - 1)).center(LINE_WIDTH), end=EMPTY)
    print(NEWLINE * 1)
    file = open(BYE_FILE, 'r')
    for line in file:
        print(line, end=EMPTY)
    file.close()
    print(NEWLINE * 5)
    print(HYPHEN * 45)
    print("Professor  : Srinivasan Mandyam             |")
    print("Course     : CSC 520 - Python Programming   |")
    print("Student    : Jigar R. Gosalia               |")
    print("Student Id : 89753                          |")
    print("Email      : 89753.gosalia@students.itu.edu |")
    print(HYPHEN * 45)

def displayWelcome(fileNames, totalNoOfSymbols):
    """ displayWelcome displays welcome information for the PSP when PSP is launched."""
    file = open(WELCOME_FILE, 'r')
    for line in file:
        print(line, end=EMPTY)
    file.close()
    print(NEWLINE * 2)
    printSymbolInformation(fileNames, totalNoOfSymbols)
    print(NEWLINE * 2)

def printSymbolInformation(fileNames, noOfSymbols):
    """ printSymbolInformation prints information about symbols and file names from which they were loaded. """
    if (len(fileNames) > 0):
        print("\t\t\tSymbol Files   : " + "\n\t\t\t\t\t ".join(fileNames))
    else:
        print("\t\t\tSymbol Files   : " + "\n\t\t\t\t\t ".join("NoInputFiles"))
    if (noOfSymbols > 0):
        print("\t\t\tSymbols Loaded : " + str(noOfSymbols))
    else:
        print("\t\t\tSymbols Loaded : " + "No Symbols loaded")

def printSymbolHeader():
    """ printSymbolHeader prints Symbol Header. """
    print(HYPHEN * DECORATE_LENGTH)
    print("%5s | %-10s | %-80s" % ("#".center(5), "Symbol".center(10), "Security Name".center(80)))
    print(HYPHEN * DECORATE_LENGTH)

def printSymbolDetailsHeaderOnViewSymbol(count, symbol, symbolDictionary):
    """ printSymbolDetailsHeaderOnViewSymbol prints Symbol Details in header on view symbol command. """
    description = symbolDictionary.get(symbol)[0];
    if len(description) > 80:
        description = description[:80]
    print("%5d | %-10s | %-80s" % (count, symbol.center(10), description))

def displayMySymbols(userName, mySymbols, mySortedSymbols):
    """ displayMySymbols displays user's symbols """
    print(NEWLINE * 50)
    pageHeader()
    welcomeUser(userName)
    symbolTableHeader()
    if (len(mySymbols) > 0):
        serialNumber = 0
        for symbol in mySortedSymbols:
            serialNumber += 1
            symbolObj = mySymbols.get(symbol, None)
            if (serialNumber != 0 and serialNumber % 11 == 0):
                print(HYPHEN * DECORATE_LENGTH)
                print(NEWLINE * 5)
                input(ENTER_CONTINUE)
                print(NEWLINE * 50)
                pageHeader()
                welcomeUser(userName)
                symbolTableHeader()
            if (symbolObj != None):
                symbolTuple(serialNumber, symbol, symbolObj)
        print(HYPHEN * DECORATE_LENGTH)
        if len(mySymbols) == 10:
            noOfLines = 0
        else:
            noOfLines = 10 - (len(mySymbols) % 11)
        print(NEWLINE * noOfLines)
    else:
        print(NEWLINE * 5)
        print(ADD_SYMBOLS_MESSAGE.center(LINE_WIDTH), end=EMPTY)
        print((HYPHEN * (len(ADD_SYMBOLS_MESSAGE) - 1)).center(LINE_WIDTH), end=EMPTY)
        print(NEWLINE * 5)
    pageFooter(USER_MENU_LIST, USER_MENU)

def symbolTableHeader():
    """ symbolTableHeader displays Stock Symbol table header. """
    print("Last Refreshed : " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(HYPHEN * DECORATE_LENGTH)
    print("%5s | %-6s | %-10s | %-10s | %-10s | %-28s | %-10s | %-10s" \
            % ("#".center(5), "Symbol".center(6), "Open Price".center(10), \
            "Price".center(10), "Change".center(10), "Trade Date Time".center(28), \
            "Days High".center(10), "Days Low".center(10)))
    print(HYPHEN * DECORATE_LENGTH)

def symbolTuple(serialNumber, symbol, symbolObj):
    """ symbolTable displays symbol tuple with Symbol Details. """
    print("%5s | %-6s | %-10s | %-10s | %-10s | %-28s | %-10s | %-10s" \
        % (str(serialNumber).center(5), symbol.center(6), formatData(DOLLAR, symbolObj.getOpenPrice(), 10), \
        formatData(DOLLAR, symbolObj.getPrice(), 10), formatData(DOLLAR, symbolObj.getChange(), 10), \
        formatData(EMPTY, symbolObj.getTradeDateTime(), 28), formatData(DOLLAR, symbolObj.getDaysHigh(), 10), \
        formatData(DOLLAR, symbolObj.getDaysLow(), 10)))

def formatData(prefix, data, value):
    """ formatData formats data and displays in formatted pattern. """
    if data != INFO_UNAVAILABLE:
        return (prefix + data).center(value)
    else:
        return data.center(value)

def displaySymbol(symbolObj, symbolDictionary):
    """ displaySymbol displays symbol's details information. """
    noData = True
    columnOne = ["Open Price", "Price", "Change", "Trade Date Time", "Days High", \
                 "Days Low", "Volume", "Previous Close", "Average Daily Volume", \
                 "Stock Exchange", "Market Cap", "Book Value", "Dividend Yield", \
                 "Dividend Share", "Year High", "Year Low", "Price Earnings Ratio", \
                 "Price Earnings Growth Ratio", "Price Sales", "Price Book", "Short Ratio"]
    columnTwo = [symbolObj.getOpenPrice(), symbolObj.getPrice(), symbolObj.getChange(), \
                 symbolObj.getTradeDateTime(), symbolObj.getDaysHigh(), symbolObj.getDaysLow(), \
                 symbolObj.getVolume(), symbolObj.getPreviousClose(), symbolObj.getAverageDailyVolume(), \
                 symbolObj.getStockExchange(), symbolObj.getMarketCap(), symbolObj.getBookValue(), \
                 symbolObj.getDividendYield(), symbolObj.getDividendShare(), symbolObj.getYearHigh(), \
                 symbolObj.getYearLow(), symbolObj.getPriceEarningsRatio(), symbolObj.getPriceEarningsGrowthRatio(), \
                 symbolObj.getPriceSales(), symbolObj.getPriceBook(), symbolObj.getShortRatio()]
    for c1, c2 in zip(columnOne, columnTwo):
        if c2 != INFO_UNAVAILABLE:
            noData = False
        print("\t\t\t\t %-30s \t %-20s" % (c1.ljust(9), c2))
    print(NEWLINE * 1)
    if noData:
        print(INTERNET_CONNECTION_ERROR.center(LINE_WIDTH))
    input(ENTER_GO_BACK)

#-----------------------
# Data Validator Methods
#-----------------------
def validFile(fileName):
    """ validFile checks whether given file is a valid Stock Symbol file and has Stock Symbols in expected format. """
    noOfSymbols = 0
    isValid = False
    if len(fileName) > 0 and os.path.exists(fileName):
        with open(fileName) as file:
            symbolList = file.read().splitlines()
        file.close()
        for line in symbolList:
            if (line.count(PIPE) == 7):
                symbolAttributes = line.split(PIPE)
                symbol = symbolAttributes[0]
                if (len(symbol) > 0 and (symbol.upper() == symbol)):
                    noOfSymbols += 1
    if (noOfSymbols > 0):
        isValid = True
    return isValid

def isValidSymbol(command, sortedSymbols):
    """ isValidSymbol checks whether given command has Stock Symbol name and it is in the loaded Stock Symbols. """
    return ((len(command.strip()) > 0) and command.strip().upper() in sortedSymbols)

def isSymbolNumber(command, sortedSymbols):
    """ isSymbolNumber checks whether given command has Stock Symbol number and it is in the loaded Stock Symbols. """
    return ((len(command.strip()) > 0) and command.strip().isdigit() and int(command.strip()) < len(sortedSymbols))


#-------------------------------------------------
# Yahoo! Finance and Symbol Object related Methods
#-------------------------------------------------
def getSymbol(symbol):
    """ Populate Symbol Object with data collected from Yahoo! Finance API. """
    symbolObj = Symbol(symbol)
    data = yahooFinanceShare(symbol)
    if (data != None):
        openPrice = action(symbol, data.get_open)
        price = action(symbol, data.get_price)
        change = action(symbol, data.get_change)
        tradeDateTime = action(symbol, data.get_trade_datetime)
        daysHigh = action(symbol, data.get_days_high)
        daysLow = action(symbol, data.get_days_low)
        symbolObj = Symbol(symbol, openPrice, price, change, tradeDateTime, daysHigh, daysLow)
    return symbolObj

def getSymbolDetails(symbol):
    """ Populate Detailed Symbol Object with data collected from Yahoo! Finance API. """
    symbolObj = Symbol(symbol)
    data = yahooFinanceShare(symbol)
    if (data != None):
        openPrice = action(symbol, data.get_open)
        price = action(symbol, data.get_price)
        change = action(symbol, data.get_change)
        tradeDateTime  = action(symbol, data.get_trade_datetime)
        daysHigh = action(symbol, data.get_days_high)
        daysLow = action(symbol, data.get_days_low)
        volume = action(symbol, data.get_volume)
        previousClose = action(symbol, data.get_prev_close)
        averageDailyVolume = action(symbol, data.get_avg_daily_volume)
        stockExchange = action(symbol, data.get_stock_exchange)
        marketCap = action(symbol, data.get_market_cap)
        bookValue = action(symbol, data.get_book_value)
        dividendShare = action(symbol, data.get_dividend_share)
        dividendYield = action(symbol, data.get_dividend_yield)
        earningsShare = action(symbol, data.get_earnings_share)
        yearHigh = action(symbol, data.get_year_high)
        yearLow = action(symbol, data.get_year_low)
        priceEarningsRatio = action(symbol, data.get_price_earnings_ratio)
        priceEarningsGrowthRatio = action(symbol, data.get_price_earnings_growth_ratio)
        priceSales = action(symbol, data.get_price_sales)
        priceBook = action(symbol, data.get_price_book)
        shortRatio = action(symbol, data.get_short_ratio)
        symbolObj = Symbol(symbol, openPrice, price, change, tradeDateTime, daysHigh, daysLow, \
                     volume, previousClose, averageDailyVolume, stockExchange, marketCap, \
                     bookValue, dividendShare, dividendYield, earningsShare, yearHigh, yearLow, \
                     priceEarningsRatio, priceEarningsGrowthRatio, priceSales, priceBook, shortRatio)
    return symbolObj

def action(symbol, callback):
    """ Populate individual property of Stock Symbol. """
    value = None
    try:
        value = callback()    
    except Exception as exception:
        dumpLogs("exception", symbol, ["Calling " + str(callback), "Exception: " + repr(exception)])
    return value

#--------------------
# Yahoo! Finance APIs
#--------------------
def yahooFinanceShare(symbol):
    """ Yahoo! Finance API for retrieving data for given Stock Symbol. """
    data = None
    try:
        data = Share(symbol)
    except ConnectionAbortedError as connection:
        dumpLogs("error", symbol, ["Fetching " + symbol, "ConnectionAbortedError: Please check your internet connection!!"])
    except TimeoutError as timeout:
        dumpLogs("error", symbol, ["Fetching " + symbol, "TimeoutError: Timeout error, try again!!"])
    except Exception as exception:
        dumpLogs("exception", symbol, ["Fetching " + symbol, "Exception: " + repr(exception)])
    return data

#-------------------------------------------------------------------------------
# Methods related to reading and writting User's preferred Stock Symbols to file
#-------------------------------------------------------------------------------
def readMySymbols(fileName):
    """ Read user saved/preferred Stock Symbols from file for displaying it on to User's Dashboard. """
    mySymbols = {}
    if (os.path.exists(fileName)):
        file = open(fileName, 'r')
        for line in file.read().split(NEWLINE):
            symbol = readFormattedSymbol(line)
            if symbol != None:
                name = symbol.getName()
                mySymbols[name] = symbol
        file.close()
    return mySymbols

def saveMySymbols(userName, mySymbols, fileName):
    """ Persist user's preferred stock symbols in file so that they can be retrieved when user logs in again. """
    if (len(userName) != 0 and doesUserExists(userName)):
        file = open(fileName, 'w')
        for symbol in (mySymbols.keys()):
            file.write(formattedSymbol(mySymbols.get(symbol)) + NEWLINE)
        file.close()

def formattedSymbol(symbolObj):
    """ Format symbol for writing into the file. """
    data = symbolObj.getName() + PIPE + \
           symbolObj.getOpenPrice() + PIPE + \
           symbolObj.getPrice() + PIPE + \
           symbolObj.getChange() + PIPE + \
           symbolObj.getTradeDateTime() + PIPE + \
           symbolObj.getDaysHigh() + PIPE + \
           symbolObj.getDaysLow()
    return data

def readFormattedSymbol(line):
    """ Read formatted symbol so that they can be displayed on User's dashboard. """
    symbol = None
    if (line.count(PIPE) == 6):
        attributes = line.split(PIPE)
        symbol = getSymbol(attributes[0])
        if INFO_UNAVAILABLE in symbol.getPrice():
            symbol = Symbol(attributes[0], attributes[1], attributes[2], \
                            attributes[3], attributes[4], attributes[5], attributes[6])
    return symbol

#----------------------------------------
# User Account/Validation related methods
#----------------------------------------
def createUser(baseDirectory):
    """ createUser creates account. """
    status = False
    print(NEWLINE * 50)
    pageHeader()
    print(NEWLINE * 10)
    userName = getValidUserName()
    if userName != EMPTY:
        print(NEWLINE * 1)
        password = getValidPassword()
        if password != EMPTY:
            print(NEWLINE * 1)
            pin = getPin(False)
            write(encrypt(password), baseDirectory, userName, PASSWORD_FILE)
            write(encrypt(pin), baseDirectory, userName, PIN_FILE)
            print(NEWLINE * 2)
            print("\t\t\t\t\t\t" + userName + " successfully created!!")
            print(NEWLINE * 2)
            status = True
    return status

def getValidUserName():
    """ getValidUserName checks if the username entered by user is an already existing user or not.
        It is used during account creation. """
    validUserName = False
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        userName = input("\t\t\t\t\t\tEnter user name : ")
        if userName != None and len(userName) != 0 and not isReservedWord(userName):
            if (doesUserExists(userName)):
                print(NEWLINE * 1)
                print("\t\t\t\tERROR : " + userName + " is already in use, try different user name!")
                print(NEWLINE * 1)
                print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
                print(NEWLINE * 1)
            else:
                validUserName = True
                break
        else:
            print(NEWLINE * 1)
            print("\t\t\t\tERROR : " + userName + " can't be used as user name, try different user name!")
            print(NEWLINE * 1)
            print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
            print(NEWLINE * 1)
    if validUserName:
        return userName
    return EMPTY

def getValidPassword():
    """ getValidPassword gets password and confirm password from the user. """
    validPassword = False
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        password = input("\t\t\t\t\tEnter password (characters > 8) : ")
        print(NEWLINE * 1)
        confirmPassword = input("\t\t\t\t\tConfirm password (characters > 8) : ")
        if (len(password) > 8 and password == confirmPassword):
            validPassword = True
            break
        else:
            if len(password) <= 8:
                print(NEWLINE * 1)
                print("\t\t\t\tERROR : password is less than 8 characters, try again!")
                print(NEWLINE * 1)
                print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
                print(NEWLINE * 1)
            else:
                print(NEWLINE * 1)
                print("\t\t\t\tERROR : password and confirm password doesn't match, try again!")
                print(NEWLINE * 1)
                print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
                print(NEWLINE * 1)
    if validPassword:
        return password
    return EMPTY

def getPin(forReset):
    """ getPin gets pin from the user.
        forReset is used to distinguish between getting pin during account creation and resetting password. """
    pin = EMPTY
    if forReset:
        pin = input("\t\t\t\t\tEnter your pin for reseting password : ")
    else:
        pin = input("\t\t\t\t\tEnter pin (useful for reset password) : ")
    return pin

def getExistingUserName():
    """ getExistingUserName gets the userName from user and verifies whether its an existing user or not. """
    existingUserName = False
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        userName = input("\t\t\t\t\t\tEnter user name : ")
        if (isReservedWord(userName) or (not doesUserExists(userName))):
            print(NEWLINE * 1)
            print("\t\t\t\t\tERROR : " + userName + " is not valid username, try again!")
            print(NEWLINE * 1)
            print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
            print(NEWLINE * 1)
        else:
            existingUserName = True
            break
    if existingUserName:
        return userName
    return EMPTY

def getNewPassword():
    """ getNewPassword gets the new password from user. """
    validPassword = False
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        attempts += 1
        password = input("\t\t\t\t\t\tEnter new password : ")
        print(NEWLINE * 1)
        confirmPassword = input("\t\t\t\t\t\tConfirm new password : ")
        if (password == confirmPassword and len(password) > 8):
            validPassword = True
            break
        else:
            print(NEWLINE * 1)
            print("\t\tERROR : password and confirm password doesn't match or password is less than 8 characters, try again!")
            print(NEWLINE * 1)
            print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
            print(NEWLINE * 1)
    if validPassword:
        return password
    return EMPTY

def resetPassword(baseDirectory):
    """ resetPassword helps in resetting password for the user. """
    status = False
    print(NEWLINE * 50)
    pageHeader()
    print(NEWLINE * 10)
    userName = getExistingUserName()
    if userName != EMPTY:
        attempts = 0
        while attempts < 3:
            attempts += 1
            print(NEWLINE * 1)
            pin = getPin(True)
            if isPinCorrect(userName, pin, baseDirectory):
                print(NEWLINE * 1)
                password = getNewPassword()
                if password != EMPTY:
                    write(encrypt(password), baseDirectory, userName, PASSWORD_FILE)
                    print(NEWLINE * 2)
                    print("\t\t\t\t\t\t" + userName + "'s password successfully reset!!")
                    print(NEWLINE * 2)
                    status = True
                break
            else:
                print(NEWLINE * 1)
                print("\t\t\t\t\t\tERROR : Incorrect pin, try again!")
                print(NEWLINE * 1)
                print("\t\t\t\t\t\tALERT : " + str(MAX_ATTEMPTS - attempts) + " attempts left!")
                print(NEWLINE * 1)
    return status

def write(data, baseDirectory, userName, name):
    """ write writes given data to file, if baseDirectory doesn't exists then it creates the base directory.
        This is used to write user specific data. """
    userDirectory = baseDirectory + os.sep + userName
    if not os.path.exists(userDirectory):
        os.mkdir(userDirectory)
    fileName = userDirectory + os.sep + name
    file = open(fileName, 'w')
    file.write(data)
    file.close()

def isReservedWord(word):
    """ isReservedWord checks if the given word is not a reserved word, if it is then it can't be used as an user name. """
    return (word != None and len(word) > 0 and word.lower() in [SYMBOLS, DATABASE, CONTENT, LOGS])

def doesUserExists(userName):
    """ doesUserExists checks if the given userName exists or not. """
    if userName != None and len(userName) > 0:
        baseDirectory = os.getcwd() + os.sep + DATABASE
        for file in os.listdir(baseDirectory):
            if (os.path.isdir(baseDirectory + os.sep + file) and file == userName):
                return True
    return False

def encrypt(rawData):
    """ encrypt converts the given rawData into an encrypted data so that its not directly human readable. """
    encrypted = EMPTY
    for character in rawData:
        newOrdinalValue = ord(character) + CONSTANT
        while True:
            if newOrdinalValue >= 33 and newOrdinalValue <= 126:
                break
            elif newOrdinalValue < 33:
                newOrdinalValue += 33
            elif newOrdinalValue > 127:
                newOrdinalValue = newOrdinalValue % 127
        encrypted = chr(newOrdinalValue) + encrypted
    return encrypted

def checkCredentials(userName, password, baseDirectory):
    """ checkCredentials checks userName and associated password with the one persisted during account creation. """
    if (doesUserExists(userName)):
        if (isPasswordCorrect(userName, password, baseDirectory)):
            return True
        else:
            print("\t\t\t\t\t\tERROR : Invalid Password, try again!", end="\n")
    else:
        print("\t\t\t\tERROR : " + userName + " doesn't exists, please try again or sign up!", end="\n")
    return False

def isPasswordCorrect(userName, password, baseDirectory):
    """ isPasswordCorrect validates user given password with the one persisted during account creation. """
    userDirectory = baseDirectory + os.sep + userName
    fileName = userDirectory + os.sep + PASSWORD_FILE
    if (os.path.exists(fileName)):
        file = open(fileName, 'r')
        encryptedPassword = file.read()
        file.close()
        if (encryptedPassword == encrypt(password)):
            return True
    return False

def isPinCorrect(userName, pin, baseDirectory):
    """ isPinCorrect validates user given pin with the one persisted during account creation. """
    userDirectory = baseDirectory + os.sep + userName
    fileName = userDirectory + os.sep + PIN_FILE
    if (os.path.exists(fileName)):
        file = open(fileName, 'r')
        existingPin = file.read()
        file.close()
        if (existingPin == encrypt(pin)):
            return True
    return False

#----------------
# Logging Methods
#----------------
def dumpLogs(eType, symbol, data):
    """ Dump error or exceptions logs in Logs directory. """
    timestamp = datetime.now()
    fileName = eType + HYPHEN + symbol + HYPHEN + timestamp.strftime("%Y%m%d-%H%M%S") + ".log"
    file = open(LOGS_DIRECTORY + os.sep + fileName, 'a')
    file.write(str(timestamp) + "\n")
    for line in data:
        file.write(line + "\n")
    file.write(HYPHEN * 150)
    file.close()
