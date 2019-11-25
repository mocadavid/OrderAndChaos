from unittest import TestCase

from Model.Entities import Move
from Repository.Repo import Table
from Service.Controller import ServiceComputer, ServiceGame


class TestServiceGame(TestCase):
    table=Table()
    serviceComputer=ServiceComputer(table)
    player=0
    serviceGame=ServiceGame(player,serviceComputer)
    move1=Move(1,1,"x")
    move2 = Move(1, 2, "x")
    move3 = Move(1, 3, "x")
    move4 = Move(1, 4, "x")
    move5 = Move(1, 5, "x")

    serviceComputer.repo.add(move1)
    serviceComputer.repo.add(move2)
    serviceComputer.repo.add(move3)
    serviceComputer.repo.add(move4)
    serviceComputer.repo.add(move5)

    def test_checkFinal(self):
        self.assertEqual(self.serviceGame.checkFinal(),1)
