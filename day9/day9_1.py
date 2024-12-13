
def get_first_form(file):
    length = len(file)
    new_code = []
    j = 0
    for i in range(length):
        if i == 0:
            for x in range(int(file[i])):
                new_code.append( "0" )
            j+=1
        elif i % 2 == 0:
            for x in range(int(file[i])):
                new_code.append( f"{j}" )
            j+=1
        else:
            for x in range(int(file[i])):
                new_code.append( "." )
    return new_code

def get_second_form(file):
    for i in range(len(file)-1,-1,-1):
        if file[i] != '.':
            index_empty = file.index(".")
            file[index_empty] = file[i]
            if "." not in file[:i]:
                return file[:i]

def get_sum(file):
    suma =0
    for i in range(len(file)):
        suma+=i*int(file[i])
    return suma

with open("data.txt",'r') as file:
    file = file.read()
    
    file = get_first_form(file)
    print(file)
    file = get_second_form(file)
    print(file)
    print(get_sum(file))
    