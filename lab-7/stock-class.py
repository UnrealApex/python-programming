class Stock:
    def __init__(self, symbol, name, previousPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice
        
    def getStockName(self):
        """return stock name for a given instance"""
        return self.__name
    
    def getStockSymbol(self):
        """return stock symbol"""
        return self.__symbol
    
    def getPreviousPrice(self):
        """return previous stock price"""
        return self.__previousPrice
    
    def setPreviousPrice(self, price):
        """set the previous price to a given value and return it"""
        self.__previousPrice = price
        return self.__previousPrice
    
    def getCurrentStockPrice(self):
        """return the curent stock price"""
        return self.__currentPrice
    
    def setCurrentStockPrice(self, price):
        """set the current stock price to a given value and return it"""
        self.__currentPrice = price
        return self.__currentPrice
    
    def getPercentChange(self):
        """print the percent change between the new and old stock prices"""
        print(f"Percentage change between the previous stock closing price and the current price for {self.__name} is {(self.__currentPrice / self.__previousPrice):.2f}%")
    
# create a stock instance for Intel stock    
intel = Stock("INTC", "Intel Corporation", 20.5, 20.35)
# get the percent change of the Intel stock instance
print(intel.getPercentChange())
