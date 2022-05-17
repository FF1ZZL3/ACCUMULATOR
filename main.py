from OPERATIONS.Text import *
from OPERATIONS.HEX import *
from OPERATIONS.OPCODE import *
from COMPONENTS.ACCUMULATOR import *
from COMPONENTS.ALU import *
from COMPONENTS.RAM import *
RAM = RAM()
ALU = ALU()
HEX = HEX()
OPCODE = OPCODE()
text=Text("deneme.txt")
ACC = ACCUMULATOR() #ACCUMULATORU 0'DAN BASLATIYOZ HER ÇALIŞTIRILDIĞINDA 0'A EŞİT OLACAK
print("before operations acc = " , ACC.getAccVal())
for i in range(1,text.total_of_row()+1):  #bu for her satır işlemi için tamamlanacak olan for.
    line=text.getting_line(i)
    opcode_STR, reg_STR=OPCODE.obtain_opcode_str(line)
    RAM.AddAdresses(reg_STR)
    opcode_BIN=OPCODE.obtain_opcode_bin(opcode_STR)
    opcode_HEX=HEX.obtain_opcode_hex(opcode_BIN)
    HEX.AddOperations(opcode_HEX)
    ALU.operations(opcode_HEX,reg_STR,2,ACC)
    print(opcode_HEX,reg_STR)
print("after operations acc = ", ACC.getAccVal())

