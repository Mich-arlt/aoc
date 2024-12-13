from sympy import *
from sympy.solvers.solveset import linsolve

def solver(a,b,result):
    A, B = symbols('A, B')
    z = linsolve([A*a[0] + B*b[0] - result[0], A*a[1] + B*b[1] - result[1]], (A, B))
    if not str(z.args[0][0]).__contains__('/') and not str(z.args[0][1]).__contains__('/') :
        return z.args[0][0]*3+z.args[0][1]
    else:
        return 0
    
with open("data.txt",'r') as file:
    input = {}
    i=0
    for line in file:
        if len(line) > 6 and line[7] == "A":
            A = (int(line.split('X+')[1].split(',')[0]),int(line.split('Y+')[1].split('\n')[0]))
        elif len(line) > 6 and  line[7] == "B":
            B = (int(line.split('X+')[1].split(',')[0]),int(line.split('Y+')[1].split('\n')[0]))
            
        elif line[0] =="P":
            if line[-1] != "\n":
                line+="\n"
            result = (int(line.split('X=')[1].split(',')[0]),int(line.split('Y=')[1].split('\n')[0]))
            input[i] = [A,B,result]
            i+=1
        
    result = 0 
    for _,val in input.items():
        result+=(solver(val[0],val[1],val[2]))
    print(result)
        