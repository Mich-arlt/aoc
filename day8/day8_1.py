import numpy as np

with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    ant_map = np.array([list(line) for line in lines])
    values = np.unique(ant_map)
    # print(values)
    values = np.delete(values,np.where(values == '.'))
    length =len(lines)
    
    antenas = []
    og_antenas = []
    suma = 0
    for val in values:
        i_val,j_val = np.where(ant_map == val)
        # print(i_val,j_val)
        group_antenas = []
        for i in range(len(i_val)):
            for j in range(i+1,len(i_val)):
                diff_i = int(i_val[i])-int(i_val[j])
                diff_j = int(j_val[i])-int(j_val[j])
                # print(diff_i,diff_j)
                if int(i_val[i])+diff_i >= 0 and int(i_val[i])+diff_i < length and int(j_val[i])+diff_j >= 0 and int(j_val[i])+diff_j < length:
                    # print("k")
                    group_antenas.append((int(i_val[i])+diff_i,int(j_val[i])+diff_j))
                if int(i_val[j])-diff_i >= 0 and int(i_val[j])-diff_i < length and int(j_val[j])-diff_j >= 0 and int(j_val[j])-diff_j < length:
                    # print("lol")
                    group_antenas.append((int(i_val[j])-diff_i,int(j_val[j])-diff_j))
        group_antenas = list(set(group_antenas))
        antenas.extend(group_antenas)

    diff = set(antenas)          
    print(len(diff))