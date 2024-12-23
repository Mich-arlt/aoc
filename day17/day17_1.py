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
            A = int(numbers)
        elif i == 1:
            B = int(numbers)
        elif i == 2:
            C = int(numbers)
        else:
            program = numbers.replace(",",'')
        i+=1
i = 0
output_result =''
A = ((((((((((((37*8*8+22)*8+4)*8+4)*8+2)*8)*8+11)*8+3)*8+2)*8+6)*8+7)*8+2)*8+1)*8+16
A = 164278496489149
while i < len(program):
    A,B,C,output,jump =  make_operation(program[i],program[i+1],A,B,C)
    if output:
        output_result += output +','
    if jump:
        i=int(jump)
    else:
        i+=2

print(output_result[0:-1])  
print(((((((((((((37*8*8+22)*8+4)*8+4)*8+2)*8)*8+11)*8+3)*8+2)*8+6)*8+7)*8+2)*8+1)*8+16)