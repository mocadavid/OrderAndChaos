from NewExceptions.NewErrors import InvalidSymbol, InvalidRow, InvalidCollumn


class ValidMove:

    def valid(self,move):
        symbol=move.getSymbol()
        row=move.getRow()
        collumn=move.getCollumn()
        if  symbol is "x" or symbol is "o":
            pass
        else:
            raise InvalidSymbol("Invalid Symbol!")
        if row > 6 or row < 1:
            raise InvalidRow("InvalidRow!")
        if collumn > 6 or collumn < 1:
            raise InvalidCollumn("InvalidCollumn!")