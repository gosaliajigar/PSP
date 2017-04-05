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

Directory Structure:
---------------------
![directorystructure](https://cloud.githubusercontent.com/assets/5839686/24687279/d10be316-196d-11e7-842e-34f717e11d4d.png)

Screenshots:
------------

| Screens | Screenshots |
| -- | -- |
| aboutScreenshot | ![aboutscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687270/d0f27c5a-196d-11e7-9534-1cd362369335.png) |
| addSymbolCommandScreenshot | ![addsymbolcommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687271/d0f6ff64-196d-11e7-8d66-81aad1640724.png) |
| addSymbolResultScreenshot | ![addsymbolresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687272/d0f7cdfe-196d-11e7-99de-7a73b753f4d0.png) |
| adminDashboardScreenshot | ![admindashboardscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687273/d0f893c4-196d-11e7-8309-933ff151a9b9.png) |
| commandsScreenshot | ![commandsscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687274/d0f8cc36-196d-11e7-92e6-e6e22e754a2c.png) |
| deleteSymbolByNameCommandScreenshot | ![deletesymbolbynamecommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687275/d0f939d2-196d-11e7-9f20-9e4ebc6b81cb.png) |
| deleteSymbolByNameResultScreenshot | ![deletesymbolbynameresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687276/d1067412-196d-11e7-8df6-5a379807eff5.png) |
| deleteSymbolByNumberCommandScreenshot | ![deletesymbolbynumbercommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687278/d10b5bbc-196d-11e7-880f-f4ec8b3e1e4a.png) |
| deleteSymbolByNumberResultScreenshot | ![deletesymbolbynumberresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687277/d10a9ed4-196d-11e7-84f2-da647c3d612b.png) |
| listAllSymbolsScreenshot | ![listallsymbolsscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687281/d1107e62-196d-11e7-8c25-b484624b5bfb.png) |
| listSymbolByNameCommandScreenshot | ![listsymbolbynamecommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687280/d10cf1a2-196d-11e7-9b17-27ca8430bcd7.png) |
| listSymbolByNameResultScreenshot | ![listsymbolbynameresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687282/d118e714-196d-11e7-99ed-bd2e8da7c8e2.png) |
| listSymbolByNumberCommandScreenshot | ![listsymbolbynumbercommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687283/d11d1e7e-196d-11e7-94b1-fb335c30d9be.png) |
| listSymbolByNumberResultScreenshot | ![listsymbolbynumberresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687284/d11eca44-196d-11e7-9868-7f1527fc9a21.png) |
| loadFromBackupScreenshot | ![loadfrombackupscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687290/d13471fa-196d-11e7-9b86-215db58b5a75.png) |
| loginScreenshot | ![loginscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687285/d11f2728-196d-11e7-89d4-55df2894b9a1.png) |
| logoutCommandScreenshot | ![logoutcommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687286/d1243952-196d-11e7-985e-2b58fac31fe6.png) |
| refreshSymbolCommandScreenshot | ![refreshsymbolcommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687287/d12ca2ea-196d-11e7-8a84-2b2b22583aa2.png) |
| resetPasswordScreenshot | ![resetpasswordscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687288/d12fbe76-196d-11e7-9fe4-161b3c097019.png) |
| signUpMaxPasswordAttemptsReachedScreenshot | ![signupmaxpasswordattemptsreachedscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687291/d134e5d6-196d-11e7-8441-27f10d0d15c0.png) |
| signUpScreenshot | ![signupscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687289/d1320424-196d-11e7-923f-eb904a3cf293.png) |
| userDashboardScreenshot | ![userdashboardscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687292/d137fb54-196d-11e7-8785-ddf27bfce10b.png) |
| userSignInScreenshot | ![usersigninscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687296/d150a9d8-196d-11e7-9c23-dbcaa23ea7d0.png) |
| viewSymbolCommandScreenshot | ![viewsymbolcommandscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687294/d14fb3de-196d-11e7-885e-d2d5628b3bcf.png) |
| viewSymbolResultScreenshot | ![viewsymbolresultscreenshot](https://cloud.githubusercontent.com/assets/5839686/24687293/d14f64ce-196d-11e7-891e-558f6d3998b0.png) |
| welcomeScreenshot | ![welcomescreenshot](https://cloud.githubusercontent.com/assets/5839686/24687295/d1507666-196d-11e7-98ce-5dae301662fd.png) |

