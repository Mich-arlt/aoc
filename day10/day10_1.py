import numpy as np

def find_all_ways_for_0(x,y,mapa,l):
    choices = [(x,y)]
    result = 0 
    meta = []
    while choices:
        last_choice = choices.pop()
        x=last_choice[0]
        y=last_choice[1]
        if x+1 !=l and mapa[(x+1,y)] == mapa[(x,y)]+1:
            if mapa[(x+1,y)] == 9:
                if (x+1,y) not in meta:
                    result+=1
                    meta.append((x+1,y))
            else:
                choices.append((x+1,y))
        if x-1 !=-1 and mapa[(x-1,y)] == mapa[(x,y)]+1:
            if mapa[(x-1,y)] == 9 :
                if (x-1,y) not in meta:
                    result+=1
                    meta.append((x-1,y))
            else:
                choices.append((x-1,y))
        if y+1 !=l and mapa[(x,y+1)] == mapa[(x,y)]+1:
            if mapa[(x,y+1)] == 9:
                if (x,y+1) not in meta:
                    result+=1
                    meta.append((x,y+1))
            else:
                choices.append((x,y+1))
        if y-1 !=-1 and mapa[(x,y-1)] == mapa[(x,y)]+1:
            if mapa[(x,y-1)] == 9:
                if (x,y-1) not in meta:
                    result+=1
                    meta.append((x,y-1))
            else:
                choices.append((x,y-1))
    return result

with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    length = len(lines)
    mapa = np.array([list(map(int,line)) for line in lines]) 
    x,y = np.where(mapa == 0)
    result = 0
    for i,j in zip(x,y):
        result+=find_all_ways_for_0(i,j,mapa,length)
    print(result)