from texttable import Texttable

from NewExceptions.NewErrors import InvalidMove, InvalidSymbol, InvalidRow, InvalidCollumn, InvalidPlacement


class Console:

    def __init__(self,ctrlGame):
        self.ctrlGame = ctrlGame

    def mainMenuUI(self):
        turn=0
        while True:
            try:
                self.displayBoardUI()
                self.orderUI()
                turn+=1
                if self.checkEndOrderUI():
                    print("Order Won!")
                    break
                self.displayBoardUI()
                self.chaosUI()
                turn += 1
                if self.checkEndChaosUI():
                    print("Chaos Won!")
                    break
                if turn==36:
                    self.chaosWonUI()
                    break
            except ValueError as ve:
                print(ve)

    def orderUI(self):
        self.ctrlGame.ctrlComputer.makeMove()

    def chaosUI(self):
        while True:
            try:
                print("<row> <collumn> <x/o>")
                answer=input(">")
                instructions=answer.split(",")
                self.ctrlGame.ctrlHuman.addMove(instructions)
                break
            except ValueError as ve:
                print(ve)
            except InvalidMove as im:
                print(im)
            except InvalidSymbol as iss:
                print(iss)
            except InvalidRow as ir:
                print(ir)
            except InvalidCollumn as ic:
                print(ic)
            except InvalidPlacement as ip:
                print(ip)

    def chaosWonUI(self):
        print("Chaos Won!")

    def checkEndOrderUI(self):
        if self.ctrlGame.checkFinal():
            return 1

    def checkEndChaosUI(self):
        if self.ctrlGame.checkFinal():
            return 1

    def displayBoardUI(self):
        rows=self.ctrlGame.ctrlComputer.repo.getTable()
        table=Texttable()
        for row in rows:
            table.add_row(row)
        print(table.draw())
