import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter


def if_tree(robots):
    robots_set = set(robots)  
    for x, y in robots:
        if (x-1, y-1) in robots_set and (x, y-1) in robots_set and (x+1, y-1) in robots_set:
            if (x-2, y-2) in robots_set and (x-1, y-2) in robots_set and (x, y-2) in robots_set and (x+1, y-2) in robots_set and (x+2, y-2) in robots_set:
                print(f"Znaleziono choinkę skierowaną w górę z punktem {(x, y)} na górze.")
                return [True,(x,y)]

        if (x-1, y+1) in robots_set and (x, y+1) in robots_set and (x+1, y+1) in robots_set:
            if (x-2, y+2) in robots_set and (x-1, y+2) in robots_set and (x, y+2) in robots_set and (x+1, y+2) in robots_set and (x+2, y+2) in robots_set:
                print(f"Znaleziono choinkę odwróconą z punktem {(x, y)} na górze.")
                return [True,(x,y)]

        if (x-1, y) in robots_set and (x-1, y-1) in robots_set and (x-1, y+1) in robots_set:
            if (x-2, y-1) in robots_set and (x-2, y-2) in robots_set and (x-2, y) in robots_set and (x-2, y+1) in robots_set and (x-2, y+2) in robots_set:
                print(f"Znaleziono choinkę skierowaną w lewo z punktem {(x, y)} na górze.")
                return [True,(x,y)]

        if (x+1, y) in robots_set and (x+1, y-1) in robots_set and (x+1, y+1) in robots_set:
            if (x+2, y-1) in robots_set and (x+2, y-2) in robots_set and (x+2, y) in robots_set and (x+2, y+1) in robots_set and (x+2, y+2) in robots_set:
                print(f"Znaleziono choinkę skierowaną w prawo z punktem {(x, y)} na górze.")
                return [True,(x,y)]

    return False,(0,0)

def get_robot_end(p,v,n,h,w):
    x = p[0]
    y = p[1]
    
    for _ in range(n):
        if 0 <= x+v[0] <= w-1 :
            x = x+v[0]        
        elif v[0] > 0:
            x = x + v[0] - w
        elif v[0] < 0:
            x =  w + x + v[0]
            
        if 0 <= y+v[1] <= h-1 :
            y = y+v[1]        
        elif v[1] > 0:
            y = y + v[1] - h
        elif v[1] < 0:
            y =  h + y + v[1]
    return x,y


with open("data.txt",'r') as file:
    input = {}
    i=0
    for line in file:
        if line[-1] != "\n":
                line+="\n"
        p = line.split()[0]
        v = line.split()[1]
        p = (int(p.split('p=')[1].split(',')[0]),int(p.split(',')[1].split(' v')[0]))
        v = (int(v.split('v=')[1].split(',')[0]),int(v.split(',')[1].split('\n')[0]))
        input[i] = [p,v]
        i+=1
    

h=103
w=101

for i in range(5000,10000):
    result = []
    for _,val in input.items():
        p = val[0]
        v = val[1]
        result.append(get_robot_end(p,v,i,h,w))
    
    tree = if_tree(result)
    
    if tree[0] :
        macierz = np.zeros((103, 101))
        for x, y in result:
            macierz[(y,x)] = 1
        macierz[(tree[1][1],tree[1][0])] = 10
        
        plt.figure(figsize=(10, 8))
        plt.imshow(macierz, cmap='viridis', aspect='auto')
        plt.savefig(f"macierz{i}.png")  
