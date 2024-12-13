from itertools import product
def stupid_math(eq):
    result = int(eq[0])
    for i in range(1,len(eq),2):
        operator = eq[i]
        num = eq[i+1]
        
        if operator == '+':
            result+=int(num)
        else:
            result*=int(num)
    return result

def check_eq(line,combination):
    eq=[]
    for i in range(len(line)-1):
        eq.append(line[i+1])
        if i >len(combination)-1:
            break
        eq.append(combination[i])
    if stupid_math(eq) == int(line[0]):
        return int(line[0])
    return 0


with open("data.txt",'r') as file:
    suma=0
    for line in file:
        line = line.replace('\n','').replace(":",'')
        eq = line.split(' ')
        eq_marks = ['+','*']
        length = len(eq)-2
        combinations = list(product(eq_marks, repeat=length))
        for comb in combinations:
            if check_eq(eq,comb) !=0:
                suma += check_eq(eq,comb)
                break
print(suma)
