
def get_first_form(file):
    length = len(file)
    new_code = []
    j = 0
    for i in range(length):
        if i == 0:
            new_code.append(["0"]*int(file[i]))
            j+=1
        elif i % 2 == 0:
            new_code.append([f"{j}"]*int(file[i]))
            j+=1
        else:
            if file[i] != "0":
                new_code.append(["."]*int(file[i]))

    return new_code

def get_second_form(file):
    all_numbers = [sublist for sublist in file if any(element.isdigit() for element in sublist)]
    index_empty = []
    for j in range(len(all_numbers)-1,-1,-1):
            print(j)
            index_full = file.index(all_numbers[j])
            index_empty = [i for i in range(len(file)) if '.' in file[i]]
            for i_empty in index_empty:   
                if len(file[i_empty]) >= len(file[index_full]) and i_empty < index_full:
                    diff_len = (len(file[i_empty]) - len(file[index_full]))
                    full_len = len(file[index_full])    
                    file[i_empty] = file[index_full]
                    file[index_full] = ["."]*full_len
                    if diff_len >0:
                        file.insert(i_empty+1,['.'] * diff_len)
                    index_empty = []
                    break
    flat_file = [element for sublist in file for element in sublist]
    return flat_file

        

def get_sum(file):
    suma =0
    for i in range(len(file)):
        if file[i].isdigit():
            suma+=i*int(file[i])
    return suma

with open("data.txt",'r') as file:
    file = file.read()
    print("etap 1")  
    file = get_first_form(file)
    print("etap 2")   
    file = get_second_form(file)
    print("etap 3")   
    print(get_sum(file))
    