from COMPONENTS.ACCUMULATOR import *
from COMPONENTS.RAM import *
RAM = RAM()
class ALU:

    def operations(self, hex_op, memAdress, value, ACC):
        if hex_op == '0x0':
            #brz gelcek
            return
        elif hex_op == '0x1':
            #BRN GELCEK
            return
        elif hex_op == '0x2':
            ACC.LDI(value)

        elif hex_op == '0x3':
            ACC.LDM(memAdress)

        elif hex_op == '0x4':
            RAM.STR(memAdress, value)
            return
        elif hex_op == '0x5':
            #ADD gelcek
            return
        elif hex_op == '0x6':
            #SUB gelcek
            return
        elif hex_op == '0x7':
            #MUL gelcek
            return
        elif hex_op == '0x8':
            #DIV gelcek
            return
        elif hex_op == '0x9':
            #NEG gelcek
            return
        elif hex_op == '0xa':
            #LSL gelcek
            return
        elif hex_op == '0xb':
            #LSR gelcek
            return
        elif hex_op == '0xc':
            #XOR gelcek
            return
        elif hex_op == '0xd':
            #NOT gelcek
            return
        elif hex_op == '0xe':
            #AND gelcek
            return
        elif hex_op == '0xf':
            #ORR gelcek
            return
        else:
            print("Error")
            return
