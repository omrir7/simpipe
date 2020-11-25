from Definitions import *
from Instruction import *

class decode():

    def __init__(self,instruction):
        instruction.opcode = (instruction.m_inst[0:7])[::-1]
        instruction.func3 = int((instruction.m_inst[12:15])[::-1], 2)
        instruction.immd_25 = int((instruction.m_inst[25])[::-1], 2)
        instruction.m_inst=instruction.m_inst


    def decode_operands(self,instruction):
        rd = int((instruction.m_inst[7:12])[::-1], 2)
        rs1 = int((instruction.m_inst[15:20])[::-1], 2)
        rs2 = int((instruction.m_inst[20:25])[::-1], 2)
        if instruction.inst_opcode in ["LUI", "AUIPC", "JAL", "JALR", "LOAD", "ALUI", "ALU", "ALUW", "FENCE"]:
            instruction.rd_vld = True
            instruction.rd = rd
        if instruction.inst_opcode in ["JALR", "BRANCH", "LOAD", "STORE", "ALUI", "ALU", "ALUW", "FENCE"]:
            instruction.rs1_vld = True
            instruction.rs1 = rs1
        if instruction.inst_opcode in ["BRANCH", "STORE", "ALU", "ALUW"]:
            instruction.rs2_vld = True
            instruction.rs2 = rs2

    def decode_inst(self,instruction):
        if instruction.inst_opcode == "BRANCH":
            instruction.name = BRANCH[self.func3]
        elif instruction.inst_opcode == "LOAD":
            instruction.name = LOAD[self.func3]
        elif instruction.inst_opcode == "STORE":
            instruction.name = STORE[self.func3]
        elif instruction.inst_opcode == "ALUI":
            instruction.name = ALUI[self.func3]
            if instruction.name == "SRI":
                instruction.name = SRI[int(self.m_inst[30])]
        elif instruction.inst_opcode == "ALU":
            if instruction.immd_25 == 1:
                instruction.name = MULDIV[self.func3]
            else:
                instruction.name = ALU[self.func3]
            if instruction.name == "ADD_SUB":
                instruction.name = ADD_SUB[int(self.m_inst[30])]
            elif instruction.name == "SR":
                instruction.name = SR[int(self.m_inst[30])]
        elif instruction.inst_opcode == "ALUIW":
            instruction.name = ALUIW[self.func3]
        elif instruction.inst_opcode == "ALUW":
            if instruction.immd_25 == 1:
                instruction.inst_opcode = MULDIV64[self.func3]
            else:
                instruction.inst_opcode = ALUW[self.func3]
        else:
            instruction.name = instruction.inst_opcode
        self.decode_operands(instruction)


