import os

"""

Program : constants.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 - Python Programming
Prof.   : Srinivasan Mandyam

Constants for Stock Portfolio Project.

"""

SEMICOLON = ";"

NEWLINE = "\n"

TAB = "\t"

PIPE = "|"

EQUAL = "="

SPACE = " "

EMPTY = ""

HYPHEN = "-"

OF = "of"

DOLLAR = "$"

BACKUP_SYMBOLS_COUNT = 8339

ENTER_CONTINUE = "PRESS ENTER TO CONTINUE .... "

COMMAND_CONTINUE = "ENTER ANY ABOVE COMMAND TO CONTINUE .... "

COMMAND_SYMBOL_CONTINUE = "ENTER ANY ABOVE COMMAND OR SYMBOL NAME TO CONTINUE .... "

ENTER_GO_BACK = "PRESS ENTER TO GO BACK .... "

ENTER_GO_BACK_AND_LOGIN = "PRESS ENTER TO GO BACK AND LOGIN WITH YOUR CREDENTIALS .... "

ENTER_GO_BACK_AND_TRY_AGAIN = "MAX ATTEMPTS REACHED, PRESS ENTER TO GO BACK AND TRY AGAIN .... "

INFO_UNAVAILABLE = "N/A"

LINE_WIDTH = 120

LISTING_SIZE = 15

HEADER_LENGTH = 15

FOOTER_LENGTH = 2

DECORATE_LENGTH = 110

MAX_ATTEMPTS = 3

CONSTANT = 31

MAIN_MENU = {"(ABOUT)":"a", "(COMMANDS)":"c", "(SIGN UP)":"u", "(SIGN IN)":"s", "(FORGOT PASSWORD)":"f", "(QUIT)":"x|q|e"}

MAIN_MENU_LIST = ["(ABOUT)", "(COMMANDS)", "(SIGN UP)", "(SIGN IN)", "(FORGOT PASSWORD)", "(QUIT)"]

USER_MENU = {"(ADD)":"a [SYM/#]", "(DELETE)":"d [SYM/#]", "(VIEW)":"v [SYM/#]", "(REFRESH)":"r [SYM/#]", "(LIST ALL)":"l", "(LOGOUT)":"o"}

USER_MENU_LIST = ["(ADD)", "(DELETE)", "(VIEW)", "(REFRESH)", "(LIST ALL)", "(LOGOUT)"]

NO_SYMBOLS_MENU = {"(ADD)":"a [SYM]", "(DELETE)":"d [SYM/#]", "(VIEW)":"v [SYM]", "(REFRESH)":"r [SYM/#]", "(LOGOUT)":"o"}

NO_SYMBOLS_MENU_LIST = ["(ADD)", "(DELETE)", "(VIEW)", "(REFRESH)", "(LOGOUT)"]

LIST_MENU = {"(SYMBOL NAME)":"[SYM]", "(SEQUENCE NUMBER)":"[#]", "(QUIT)":"x|q|e"}

LIST_MENU_LIST = ["(SYMBOL NAME)", "(SEQUENCE NUMBER)", "(QUIT)"]

SYMBOLS = "symbols"

CONTENT = "content"

DATABASE = "database"

LOGS = "logs"

BACKUP_SYMBOLS = "backUpSymbols"

PASSWORD_FILE = "password.txt"

PIN_FILE = "pin.txt"

STOCKS_FILE = "stocks.txt"

ADMIN_PASSWORD = "admin"

ADMIN_PIN = "1234"

USER_DATABASE_DIRECTORY = os.getcwd() + os.sep + DATABASE

CONTENT_DIRECTORY = os.getcwd() + os.sep + CONTENT

SYMBOLS_DIRECTORY = os.getcwd() + os.sep + SYMBOLS

ADMIN_DIRECTORY = USER_DATABASE_DIRECTORY + os.sep + "admin" 

LOGS_DIRECTORY = os.getcwd() + os.sep + LOGS

BACKUP_SYMBOLS_DIRECTORY = os.getcwd() + os.sep + BACKUP_SYMBOLS

ADMIN_PASSWORD_FILE = ADMIN_DIRECTORY + os.sep + PASSWORD_FILE

ADMIN_PIN_FILE = ADMIN_DIRECTORY + os.sep + PIN_FILE

NASDAQ_URL = 'ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt'

OTHERS_URL = 'ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt'

NASDAQ_FILE = SYMBOLS_DIRECTORY + os.sep + "nasdaqlisted.txt"

OTHERS_FILE = SYMBOLS_DIRECTORY + os.sep + "otherlisted.txt"

BACKUP_NASDAQ_FILE = BACKUP_SYMBOLS_DIRECTORY + os.sep + "nasdaqlisted.txt"

BACKUP_OTHERS_FILE = BACKUP_SYMBOLS_DIRECTORY + os.sep + "otherlisted.txt"

ABOUT_FILE = CONTENT_DIRECTORY + os.sep + "about.txt"

COMMANDS_FILE = CONTENT_DIRECTORY + os.sep + "commands.txt"

WELCOME_FILE = CONTENT_DIRECTORY + os.sep + "welcome.txt"

BYE_FILE = CONTENT_DIRECTORY + os.sep + "bye.txt"

VALID_FILE = "Enter the path to valid symbols file: "

INTERNET_CONNECTION_ERROR = "ALERT : Check SYMBOL spelling, internet connection or some process on your host m/c is not allowing to fetch data!"

ADD_SYMBOLS_MESSAGE = "!NO SYMBOLS ADDED TO YOUR LIST, PLEASE ADD SYMBOLS TO YOUR PORTFOLIO!"

SYMBOL_FILE_NEEDED_MESSAGE = "!SYMBOL FILE NOT PRESENT SO PLEASE PROVIDE FILE NAME!"

WELCOME_HEADER = "!Welcome to Terminal Based Personal Stock Portfolio!"

THANK_YOU_HEADER = "!Thank You for using Terminal Based Personal Stock Portfolio!"
