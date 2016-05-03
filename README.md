# PSP (Personal Stock Portfolio)
Terminal Based UI Stock Portfolio

About Personal Stock Portfolio:
-------------------------------
Personal Stock Portfolio is Terminal Based UI software that loads list of Stock Symbols and gives the user capability to ...
	1. View Stock Symbols
	2. Get Stock Symbols latest information
	3. Add Stock Symbol to user's list
	4. Delete Stock Symbol from user's list
	5. Refresh Stock Symbol/Symbols information
Stock Portfolio uses Yahoo! Finance module to retrieve latest information about stock symbol.

Persistance:
------------
Personal Stock Portfolio uses file based persistence for user related data (username, password, pin and stock symbols).

Usage:
------
Read the available commands at the bottom of each screen for execution.

Sign Up for your personal account so that you can preserve your favourite Stock Symbols and view them when you login with your credentials.

By default, an account(USERNAME=admin, PASSWORD=admin & PIN=1234) is created for usage so that you don't have to worry about creating accounts.

Pre-Loaded Stock Symbols:
-------------------------
Personal Stock Portfolio software downloads list of Stock Symbols from internet, if they are not available then it loads them from back up symbol files. This means that if you try to add any Stock Symbol which is not present in this list then the software wouldn't load it.

In worst case, if back up files are also not available then any symbol you try to add, would be added as there are no stock symbols available for checking. It is possible that that Stock Symbol is not a valid symbol.

Dependencies:
-------------
	1. Pre-defined Symbols file to view list
	2. Internet connection for downloading stock symbols and Yahoo! Finance module to retrieve data

System Requirement:
-------------------
	1. Operating System : Windows
	2. Python 3.5.1 or above
	3. Python module to get Stock data from Yahoo! Finance

Installation Instructions:
--------------------------
	1. Python module for Yahoo! Finance (1.2.1) : https://pypi.python.org/pypi/yahoo-finance
	2. From command prompt run command (pip install yahoo-finance)

Restrictions:
-------------
Yahoo! Finance module (free version) retrieves data which is 15 minutes older (paid version no-delay).

Failure Points:
---------------
If internet connection is down or Yahoo! Finance server is down, there will be intermintent failures. I have tried level best to gracefully handle situation but again it is not 100% failure proof.

Reference or Credits:
---------------------
Stock Symbol files are downloaded from ftp://ftp.nasdaqtrader.com/symboldirectory/

