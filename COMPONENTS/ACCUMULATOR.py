from COMPONENTS.RAM import *
class ACCUMULATOR:
    def __init__(self):
        self.acc=0

    def LDM(self, memAdress):
        self.acc=RAM.get_Val_of_register(memAdress)

    def LDI(self, value):
        self.acc=value
    def getAccVal(self):
        print(self.acc)
        return self.acc