from NewExceptions.NewErrors import InvalidPlacement


class Table:

    def __init__(self):
        self.__table=[[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]


    def getTable(self):
        return self.__table

    def add(self,move):
        symbol=move.getSymbol()
        row=move.getRow()
        collumn=move.getCollumn()
        if self.__table[row-1][collumn-1]!=" ":
            raise InvalidPlacement("Invalid placement!")
        else:
            self.__table[row-1][collumn-1]=symbol
