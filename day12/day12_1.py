import numpy as np

def get_walls_and_neib(field,l):
    field_info ={}
    walls=0
    for i in range(l):
        for j in range(l):
            neib =set()
            if i-1 >= 0:
                if field[i-1,j] == field[i,j]:
                    neib.add((i-1,j))
                else:
                    walls+=1
            else:
                walls+=1

            if j-1 >= 0:
                if field[i,j-1] == field[i,j]:
                    neib.add((i,j-1))
                else:
                    walls+=1
            else:
                walls+=1

            if i+1 <= l-1:
                if field[i+1,j] == field[i,j]:
                    neib.add((i+1,j))
                else:
                    walls+=1
            else:
                walls+=1
                
            if j+1 <= l-1:
                if field[i,j+1] == field[i,j]:
                    neib.add((i,j+1))
                else:
                    walls+=1
            else:
                walls+=1
            if j==0 and i==0:
                field_info[field[i,j]] = [1,walls,neib]
            else:
                state = False
                for key, value in field_info.items():
                    neib_new = value[2]
                    if (i,j) in neib_new:
                        field_info[key][0]+=1
                        field_info[key][1]+=walls 
                        field_info[key][2].update(neib)
                        state = True
                        break
                if state == False:
                    if field[i,j] in field_info:
                        field_info[field[i,j]+f"{i,j}"+"hej"] = [1,walls,neib] 
                    else:
                        field_info[field[i,j]] = [1,walls,neib]

            walls = 0
            neib =set()


    return field_info

def delete_dup(field_info):
    result = []
    for key1,_ in field_info.items():
        for key2,_ in field_info.items():
            if key1 != key2 and len(key2) != 1 and key1 not in result and key2 not in result:
                if len(field_info[key1][2] & field_info[key2][2]) > 0:
                    field_info[key1][0]+=field_info[key2][0]
                    field_info[key1][1]+=field_info[key2][1] 
                    field_info[key1][2].update(field_info[key2][2])
                    result.append(key2)
    for key in set(result):
        field_info.pop(key)    
    return field_info  

with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    length =len(lines)
    field = np.array([list(line) for line in lines])
    field_info = get_walls_and_neib(field,length)
    field_info = delete_dup(field_info)
    result = 0
    for key,value in field_info.items():
        result+=value[0]*value[1]
    print(result)