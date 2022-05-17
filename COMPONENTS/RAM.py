class RAM:
    def __init__(self):
        self.Reg_Dict = {}
        self.Reg_Order = 0

    def AddAdresses(self, reg_STR):
        Add_Reg_STR = reg_STR
        self.Reg_Dict[Add_Reg_STR] = 0
    def showAdresses(self):
        return self.Reg_Dict

    def get_Val_of_register(self, reg_STR):
        return self.Reg_Dict[reg_STR]

    def STR(self, reg_STR, value):
        self.Reg_Dict[reg_STR]=value