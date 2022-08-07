import unittest

class main:
    def __init__(self,number=0):
        self.number = number

    def sum(self,number):
        return self.number + number

    def getNumber(self):
        return self.number

class TestGetSum(unittest.TestCase):
    def runTest(self) :
        M = main(5)
        Value = M.sum(5)
        self.assertEquals(M.getNumber(),Value)


unittest.main()