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
    og_points =[]
    for val in values:
        i_val,j_val = np.where(ant_map == val)
        group_antenas = []
        for i in range(len(i_val)):
            for j in range(i+1,len(i_val)):
                diff_i = int(i_val[i])-int(i_val[j])
                diff_j = int(j_val[i])-int(j_val[j])
                if int(i_val[i])+diff_i >= 0 and int(i_val[i])+diff_i < length and int(j_val[i])+diff_j >= 0 and int(j_val[i])+diff_j < length:
                    a = 1
                    while int(i_val[i])+diff_i*a >= 0 and int(i_val[i])+diff_i*a < length and int(j_val[i])+diff_j*a >= 0 and int(j_val[i])+diff_j*a < length:
                        group_antenas.append((int(i_val[i])+diff_i*a,int(j_val[i])+diff_j*a))
                        a+=1
                if int(i_val[i])-diff_i >= 0 and int(i_val[i])-diff_i < length and int(j_val[i])-diff_j >= 0 and int(j_val[i])-diff_j < length:
                    a = 1
                    while int(i_val[i])-diff_i*a >= 0 and int(i_val[i])-diff_i*a < length and int(j_val[i])-diff_j*a >= 0 and int(j_val[i])-diff_j*a < length:
                        group_antenas.append((int(i_val[i])-diff_i*a,int(j_val[i])-diff_j*a))
                        a+=1
                og_points.append((int(i_val[i]),int(j_val[i])))
        group_antenas = list(set(group_antenas))
        antenas.extend(group_antenas)
        antenas.extend(og_points)

    print(len(set(antenas)))