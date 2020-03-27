import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
POP = 0b01000110
RET = 0b00010001
ADD = 0b10100000
CMP = 0b10100111
JMP = 0b01010100
JNE = 0b01010110
JEQ = 0b01010101

CALL = 0b01010000
PUSH = 0b01000101

class CPU:
    def __init__(self):
        """Construct A New CPU"""
        self.registers = [0] * 8
        self.ram = [0] * 256
        self.pc = 0
        self.sp = 7
        self.registers[7] = 0xF4
        self.flags = {}
        self.branch_table = {}
        self.branch_table[ADD] = self.add
        self.branch_table[LDI] = self.ldi
        self.branch_table[PRN] = self.prn
        self.branch_table[MUL] = self.mul
        self.branch_table[PUSH] = self.push
        self.branch_table[POP] = self.pop
        self.branch_table[CALL] = self.call
        self.branch_table[RET] = self.ret
        self.branch_table[JMP] = self.jmp
        self.branch_table[JNE] = self.jne
        self.branch_table[JEQ] = self.jeq
        self.branch_table[CMP] = self.cmp_fun