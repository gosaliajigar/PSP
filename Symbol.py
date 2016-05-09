import constants

"""

Program : Symbol.py
Author  : Jigar R. Gosalia
Verion  : 1.0
Course  : CSC-520 - Python Programming
Prof.   : Srinivasan Mandyam

Symbol Class that will hold all the properties related to Stock Symbol.

"""

class Symbol(object):

    def __init__(self, name, openPrice=None, price=None, change=None, tradeDateTime=None, daysHigh=None, daysLow=None, \
                 volume=None, previousClose=None, averageDailyVolume=None, stockExchange=None, marketCap=None, \
                 bookValue=None, dividendShare=None, dividendYield=None, earningsShare=None, yearHigh=None, yearLow=None, \
                 priceEarningsRatio=None, priceEarningsGrowthRatio=None, priceSales=None, priceBook=None, shortRatio=None):
        """ Constructor """
        self._name = checkVariable(name, False)
        self._openPrice = checkVariable(openPrice, True)
        self._price = checkVariable(price, True)
        self._change = checkVariable(change, True)
        self._tradeDateTime = checkVariable(tradeDateTime, False)
        self._daysHigh = checkVariable(daysHigh, True)
        self._daysLow = checkVariable(daysLow, True)
        self._volume = checkVariable(volume, False)
        self._previousClose = checkVariable(previousClose, True)
        self._averageDailyVolume = checkVariable(averageDailyVolume, False)
        self._stockExchange = checkVariable(stockExchange, False)
        self._marketCap = checkVariable(marketCap, False)
        self._bookValue = checkVariable(bookValue, True)
        self._dividendShare = checkVariable(dividendShare, False)
        self._dividendYield = checkVariable(dividendYield, False)
        self._earningsShare = checkVariable(earningsShare, False)
        self._yearHigh = checkVariable(yearHigh, True)
        self._yearLow = checkVariable(yearLow, True)
        self._priceEarningsRatio = checkVariable(priceEarningsRatio, True)
        self._priceEarningsGrowthRatio = checkVariable(priceEarningsGrowthRatio, False)
        self._priceSales = checkVariable(priceSales, True)
        self._priceBook = checkVariable(priceBook, True)
        self._shortRatio = checkVariable(shortRatio, False)

    # Accessor Methods
    def getName(self):
        return self._name

    def getOpenPrice(self):
        return self._openPrice

    def getPrice(self):
        return self._price

    def getChange(self):
        return self._change

    def getTradeDateTime(self):
        return self._tradeDateTime

    def getDaysHigh(self):
        return self._daysHigh

    def getDaysLow(self):
        return self._daysLow

    def getVolume(self):
        return self._volume

    def getPreviousClose(self):
        return self._previousClose

    def getAverageDailyVolume(self):
        return self._averageDailyVolume

    def getStockExchange(self):
        return self._stockExchange

    def getMarketCap(self):
        return self._marketCap

    def getBookValue(self):
        return self._bookValue

    def getDividendShare(self):
        return self._dividendShare

    def getDividendYield(self):
        return self._dividendYield

    def getEarningsShare(self):
        return self._earningsShare

    def getYearHigh(self):
        return self._yearHigh

    def getYearLow(self):
        return self._yearLow

    def getPriceEarningsRatio(self):
        return self._priceEarningsRatio

    def getPriceEarningsGrowthRatio(self):
        return self._priceEarningsGrowthRatio

    def getPriceSales(self):
        return self._priceSales

    def getPriceBook(self):
        return self._priceBook

    def getShortRatio(self):
        return self._shortRatio

    def __str__(self):
        """ String Presentation """
        return "Symbol[" \
               + "name=" + self._name + constants.SEMICOLON \
               + "openPrice=" + self._openPrice + constants.SEMICOLON \
               + "price=" + self._price + constants.SEMICOLON \
               + "change" + self._change + constants.SEMICOLON \
               + "tradeDateTime=" + self._tradeDateTime + constants.SEMICOLON \
               + "daysHigh=" + self._daysHigh + constants.SEMICOLON \
               + "daysLow=" + self._daysLow + constants.SEMICOLON \
               + "volume=" + self._volume + constants.SEMICOLON \
               + "previousClose=" + self._previousClose + constants.SEMICOLON \
               + "averageDailyVolume=" + self._averageDailyVolume + constants.SEMICOLON \
               + "stockExchange=" + self._stockExchange + constants.SEMICOLON \
               + "marketCap=" + self._marketCap + constants.SEMICOLON \
               + "bookValue=" + self._bookValue + constants.SEMICOLON \
               + "dividendShare=" + self._dividendShare + constants.SEMICOLON \
               + "dividendYield=" + self._dividendYield + constants.SEMICOLON \
               + "earningsShare=" + self._earningsShare + constants.SEMICOLON \
               + "yearHigh=" + self._yearHigh + constants.SEMICOLON \
               + "yearLow=" + self._yearLow + constants.SEMICOLON \
               + "priceEarningsRatio=" + self._priceEarningsRatio + constants.SEMICOLON \
               + "priceEarningsGrowthRatio=" + self._priceEarningsGrowthRatio + constants.SEMICOLON \
               + "priceSales=" + self._priceSales + constants.SEMICOLON \
               + "priceBook=" + self._priceBook + constants.SEMICOLON \
               + "shortRatio=" + self._shortRatio + "]"

def checkVariable(variable, precision):
    """ checkVariable formats the value of variable depending on whether value is
        available or not and the precision provided. """
    value = constants.INFO_UNAVAILABLE
    if (variable != None and
        len(variable) > 0 and
        variable != constants.INFO_UNAVAILABLE):
        if precision:
            floatValue = float(variable)
            formatted = ("%.2f" % (floatValue))
            value = str(formatted)
        else:
            value = variable
    return value
