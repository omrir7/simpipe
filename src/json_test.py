import json

def decode_feilds(inst,arr):
    fields=arr['fields']
    values=[0]*len(fields)
    for i in range(len(fields)):
        cur_field_bit_range=arr[fields[i]]
        values[i]=inst[cur_field_bit_range[0]:cur_field_bit_range[1]+1]
        values[i]=int(values[i], 2)
    return values,fields
#def decode_feilds_comp(inst,arr):
#    fields=arr['fields']
#    k=0
#    values=[0]*len(fields)
#    for i in range(len(fields)):
#        cur_field_bit_range=arr_tmp[fields[i]]
#        k=cur_field_bit_range[0]
#        temp=""
#        for k in cur_field_bit_range:
#            temp = temp + inst[k]
#        values[i] = int(temp, 2)
#    return values,fields
#

with open('C:/Users/omrir/PycharmProjects/simpipe/src/riscv_isa.json') as f:
    arr_tmp=json.load(f)
count=0
inst1="11100110010100000100000000000001" # jalr rd=5 rs=4 im=1
inst3="0001000011000011" # c.sw rs2=2 rs1=3 uimm2_6=0   - imm decode not implemented
inst="'01010100111000010000000000000000'" # c.srai  rs1/rd=2 uimm2_6=0  - imm decode not implemented


last=False
comp=1

if(inst[1] == "0" and inst[0]=="0"):
    arr_tmp=arr_tmp["00"]
if (inst[1] == "0" and inst[0]=="1"):
    arr_tmp = arr_tmp["01"]
if (inst[1] == "1" and inst[0]=="0"):
    arr_tmp=arr_tmp["10"]
if (inst[1] == "1" and inst[0]=="1"):
    arr_tmp=arr_tmp["11"]
    comp=0
while(last==0):
    last=arr_tmp['last_level']
    if(last==0 and comp==0):
        bit_range=arr_tmp['bit_range']
        next_feild=inst[bit_range[0]:bit_range[1]+1]
        next_feild=str(next_feild)
        arr_tmp=arr_tmp[next_feild[::-1]]
    if(last==0 and comp==1):
        bit_range = arr_tmp['bit_range']
        next_feild=inst[bit_range[0]:bit_range[1]+1]
        next_feild=str(next_feild)
        arr_tmp=arr_tmp[next_feild[::-1]]
if comp==0:
    values,fields=decode_feilds(inst,arr_tmp)
if comp==1:
    values, fields = decode_feilds(inst, arr_tmp)
name=arr_tmp['name']

print(fields)
print (values)
print(name)

