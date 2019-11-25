from Repository.Repo import Table
from Service.Controller import ServiceComputer, ServiceHuman, ServiceGame
from UI.UserInput import Console
from Validation.Validator import ValidMove

repoMoves=Table()
validMove=ValidMove()
serviceComputer=ServiceComputer(repoMoves)
serviceHuman=ServiceHuman(repoMoves,validMove)
serviceGame=ServiceGame(serviceHuman,serviceComputer)
console=Console(serviceGame)
console.mainMenuUI()