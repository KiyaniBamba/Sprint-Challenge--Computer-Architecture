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
        # self.branch_table[JMP] = self.jmp
        # self.branch_table[JNE] = self.jne
        # self.branch_table[JEQ] = self.jeq
        # self.branch_table[CMP] = self.cmp_fun

def load(self, filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = []

        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    comment_split = line.split("#")
                    num = comment_split[0].strip()

                    # Check if the current line is a blank line
                    if num == "":
                        continue

                    value = int(num, 2)

                    program.append(value)

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {filename} Not Found")
            sys.exit(1)

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    # ALU to perform arithmatic operations and also CMP operations
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        # vars to be used for flagging
        a = self.registers[reg_a]
        b = self.registers[reg_b]

        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        elif op == "MUL":
            self.registers[reg_a] *= self.registers[reg_b]
        elif op == "CMP":
            if a == b:
                self.flags['E'] = 1
            else:
                self.flags['E'] = 0
            if a < b:
                self.flags['L'] = 1
            else:
                self.flags['L'] = 0
            if a > b:
                self.flags['G'] = 1
            else:
                self.flags['G'] = 0
        else:
            raise Exception("Unsupported ALU operation") 

    def ram_read(self, MAR):
        return self.ram[MAR]

    def write_ram(self, MAR, MDR):
        self.ram[MAR] = MDR

    def jeq(self, a=None):
        if self.flags['E'] == 1:
            self.pc = self.registers[a]
        else:
            self.pc += 2

    def jmp(self, a=None):
        self.pc = self.registers[a]

    def jne(self, a=None):
        if self.flags['E'] == 0:
            self.pc = self.registers[a]
        else:
            self.pc += 2

    def cmp_func(self, a=None, b=None):
        self.alu("CMP", a, b)

    def ldi(self, a=None, b=None):
        self.registers[a] = b

    def prn(self, a=None):
        print(self.registers[a])

    def add(self, a=None, b=None):
        self.alu("ADD", a, b)

    def mul(self, a=None, b=None):
        self.alu("MUL", a, b) 

