from Model.Entities import Move
from NewExceptions.NewErrors import InvalidMove
from random import *

class ServiceComputer:

    def __init__(self,repo):
        self.repo = repo

    def makeMove(self):
        table=self.repo.getTable()
        symbol=self.mostUsedSymbol(table)
        moveCoords=self.sameSymbol(symbol,table)
        print(moveCoords)
        move1=Move(moveCoords[0]+1,moveCoords[1]+1,symbol)
        self.repo.add(move1)

    def mostUsedSymbol(self, table):
        x=0
        o=0
        for row in range(0,6):
            for collumn in range(0,6):
                if table[row][collumn]=="x":
                    x+=1
                elif table[row][collumn]=="o":
                    o+=1
        if x>o:
            return "x"
        elif x<o:
            return "o"
        else:
            rnglist=["x","o"]
            rng=choice(rnglist)
            return rng

    def sameSymbol(self, symbol, table):
        bestmove=[0,0]
        maxNeigh=0

        for row in range(0,6):
            for collumn in range(0,6):
                if table[row][collumn] is " ":
                    neigh = 0
                    move=[row,collumn]
                    neigh=self.checkNeighbours(row,collumn,symbol,table)
                    if neigh >= maxNeigh:
                        maxNeigh=neigh
                        bestmove[0],bestmove[1]=move[0],move[1]
                        print(bestmove)

        return bestmove

    def checkNeighbours(self, row, collumn, symbol, table):
        neigh=0
        try:
            if table[row][collumn-1] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row][collumn+1] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row-1][collumn] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row+1][collumn] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row+1][collumn-1] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row-1][collumn+1] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row-1][collumn-1] is symbol:
                neigh+=1
        except IndexError:
            pass
        try:
            if table[row+1][collumn+1] is symbol:
                neigh+=1
        except IndexError:
            pass
        return neigh


class ServiceHuman:

    def __init__(self,repo,valid):
        self.valid = valid
        self.repo = repo

    def addMove(self,info):
        if len(info) < 3 or len(info) > 3:
            raise InvalidMove("Invalid move!")
        row=int(info[0])
        collumn=int(info[1])
        symbol=info[2]
        move1=Move(row,collumn,symbol)
        self.valid.valid(move1)
        self.repo.add(move1)

class ServiceGame:

    def __init__(self,ctrlHuman,ctrlComputer):
        self.ctrlComputer = ctrlComputer
        self.ctrlHuman = ctrlHuman

    def checkFinal(self):
        table=self.ctrlComputer.repo.getTable()
        if self.lineWon(table):
            return 1
        if self.collumnWon(table):
            return 1
        if self.diagonalWon(table):
            return 1
        return 0

    def lineWon(self,table):
        for row in table:
            if row[0]is row[1] and row[1] is row[2] and row[2] is row[3] and row[3] is row[4] and row[4]!=" ":
                return 1
            elif row[4] is row[5] and row[1] is row[2] and row[2] is row[3] and row[3] is row[4] and row[4]!=" ":
                return 1
        return 0

    def collumnWon(self,table):
        for index in range(0,4):
            if table[0+index][0] is table[0+index][1] and table[0+index][1] is table[0+index][2] and table[0+index][2] is table[0+index][3] and table[0+index][3] is table[0+index][4]and table[0+index][4]!=" ":
                return 1
            elif table[0+index][4] is table[0+index][5] and table[0+index][1] is table[0+index][2] and table[0+index][2] is table[0+index][3] and table[0+index][3] is table[0+index][4] and table[0+index][4]!=" ":
                return 1
        return 0

    def diagonalWon(self,table):
        tb=table
        if tb[5][1] is tb[4][2] and tb[4][2] is tb[3][3] and tb[3][3] is tb[2][4] and tb[2][4] is tb[1][5] and tb[1][5]!=" ":
            return 1
        if tb[5][0] is tb[4][1] and tb[4][1] is tb[3][2] and tb[3][2] is tb[2][3] and tb[2][3] is tb[1][4] and tb[1][4]!=" ":
            return 1
        if tb[4][1] is tb[3][2] and tb[3][2] is tb[2][3] and tb[2][3] is tb[1][4] and tb[1][4] is tb[0][5] and tb[0][5]!=" ":
            return 1
        if tb[5][1] is tb[4][2] and tb[4][2] is tb[3][3] and tb[3][3] is tb[2][4] and tb[2][4] is tb[1][5] and tb[1][5]!=" ":
            return 1
        return 0
