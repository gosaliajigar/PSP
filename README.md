# PSP (Personal Stock Portfolio)
As part of CSC-520 Python Programming course, PSP (Terminal Based UI Personal Stock Portfolio) was developed for final term project.

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
Open psp.py in IDLE and run psp.py by pressing F5.

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
	------------------------
	Sample installation logs
	------------------------
		$ python --version
		Python 3.5.1
		
		$ pip install yahoo_finance
		Collecting yahoo-finance
		  Downloading yahoo-finance-1.2.1.zip
		Collecting pytz (from yahoo-finance)
		  Downloading pytz-2016.4-py2.py3-none-any.whl (480kB)
		←[K    100% |################################| 483kB 874kB/s ta 0:00:01
		Collecting simplejson (from yahoo-finance)
		  Downloading simplejson-3.8.2.tar.gz (76kB)
		←[K    100% |################################| 77kB 2.6MB/s
		Installing collected packages: pytz, simplejson, yahoo-finance
		  Running setup.py install for simplejson
		  Running setup.py install for yahoo-finance
		Successfully installed pytz-2016.4 simplejson-3.8.2 yahoo-finance-1.2.1
		←[33mYou are using pip version 7.1.2, however version 8.1.1 is available.
		You should consider upgrading via the 'python -m pip install --upgrade pip' command.←[0m

Restrictions:
-------------
Yahoo! Finance module (free version) retrieves data which is 15 minutes older (for instant data, use google apis).

Failure Points:
---------------
If internet connection is down or Yahoo! Finance server is down, there will be intermintent failures. 

I have tried level best to gracefully handle situation but again it is not 100% failure proof.

Reference or Credits:
---------------------
Stock Symbol files are downloaded from ftp://ftp.nasdaqtrader.com/symboldirectory/

Screenshots:
------------

| Screens | Screenshots |
| -- | -- |
| aboutScreenshot |  |
| addSymbolCommandScreenshot |  |
| addSymbolResultScreenshot |  |
| adminDashboardScreenshot |  |
| commandsScreenshot |  |
| deleteSymbolByNameCommandScreenshot |  |
| deleteSymbolByNameResultScreenshot |  |
| deleteSymbolByNumberCommandScreenshot |  |
| deleteSymbolByNumberResultScreenshot |  |
| directoryStructure |  |
| listAllSymbolsScreenshot |  |
| listSymbolByNameCommandScreenshot |  |
| listSymbolByNameResultScreenshot |  |
| listSymbolByNumberCommandScreenshot |  |
| listSymbolByNumberResultScreenshot |  |
| loadFromBackupScreenshot |  |
| loginScreenshot |  |
| logoutCommandScreenshot |  |
| refreshSymbolCommandScreenshot |  |
| resetPasswordScreenshot |  |
| signUpMaxPasswordAttemptsReachedScreenshot |  |
| signUpScreenshot |  |
| userDashboardScreenshot |  |
| userSignInScreenshot |  |
| viewSymbolCommandScreenshot |  |
| viewSymbolResultScreenshot |  |
| welcomeScreenshot |  |

