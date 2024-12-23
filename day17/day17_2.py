def adv(A,operand):
    return int(A/2**int(operand))

def bxl(B,operand):
    return B^int(operand)

def bst(operand):
    return int(operand)%8

def jnz(operand):
    return operand

def bxc(B,C):
    return B^C

def out(operand):
    return str(int(operand)%8)

def make_combo_operand(operand,A,B,C):
    if operand in ['0','1','2','3']:
        return operand
    elif operand == '4':
        return A
    elif operand == '5':
        return B
    elif operand == '6':
        return C
    

def make_operation(opcode,operand,A,B,C):
    jump = None
    output = None
    if opcode == "0":
        operand = make_combo_operand(operand,A,B,C)
        A = adv(A,operand)
    elif opcode == "1":
        B = bxl(B,operand)
    elif opcode == "2":
        operand = make_combo_operand(operand,A,B,C)
        B = bst(operand)
    elif opcode == "3":
        if A != 0:
            jump = operand
    elif opcode == "4":
        B = bxc(B,C)
    elif opcode == "5":
        operand = make_combo_operand(operand,A,B,C)
        output = out(operand)
    elif opcode == "6":
        operand = make_combo_operand(operand,A,B,C)
        B = adv(A,operand)
    elif opcode == "7":
        operand = make_combo_operand(operand,A,B,C)
        C = adv(A,operand)

    return A,B,C,output,jump




with open("data.txt",'r') as file:
    input = {}
    i=0
    A = 0
    B = 0
    C = 0
    program=''
    i = 0
    for line in file:       
        numbers = line.split(': ')[1]
        if i == 0:
            pass
        if i == 1:
            B = int(numbers)
        elif i == 2:
            C = int(numbers)
        else:
            program = numbers
        i+=1

output_result =''
print(program)
program_clear = program.replace(",",'')
a = 164278496489112
while program.strip() != output_result[0:-1].strip():
# while "3,0" != output_result[0:-1]:
    output_result =''
    i = 0
    A = a
    print(A)
    print(output_result[0:-1])
    while i < len(program_clear):
        A,B,C,output,jump =  make_operation(program_clear[i],program_clear[i+1],A,B,C)
        if output:
            output_result += output +','
        if jump:
            i=int(jump)
        else:
            i+=2
    a+=1
    
print(a-1)
print(output_result[0:-1])  

