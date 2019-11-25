class Move:

    def __init__(self,row,collumn,symbol):
        self.__collumn = collumn
        self.__row = row
        self.__symbol = symbol

    def getSymbol(self):
        return self.__symbol

    def getRow(self):
        return self.__row

    def getCollumn(self):
        return self.__collumn


