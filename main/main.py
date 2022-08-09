class main:
    def __init__(self, number=0):
        self.number = number

    def sum(self, number):
        return self.number + number

    def getNumber(self):
        return self.number

    def getNegativaNumber(self):
        result = 5
        result += self.number
        return result ^ 2
