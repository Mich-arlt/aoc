import numpy as np
import queue

def valid_move(maze,s,x,y,j,d):
    if j == "^" and x-1 >=0 and d != "v":
        if maze[x-1,y] == 0:
            s+=1
            x = x-1
            return (s,x,y,'^')
    elif j == "v" and x+1 < maze.shape[0] and d != "^":
        if maze[x+1,y] == 0:
            s+=1
            x = x+1
            return (s,x,y,'v')
    elif j == "<" and y-1 >=0 and d != ">":
        if maze[x,y-1] == 0:
            s+=1
            y = y-1
            return (s,x,y,'<')
    elif j == ">" and y+1 < maze.shape[0] and d != "<":
        if maze[x,y+1] == 0:
            s+=1
            y = y+1
            return (s,x,y,'>')
    return None


with open("data.txt",'r') as file:
    maze = np.zeros((71,71))
    next_bits = []
    i=0
    for line in file:
        line = line.replace('\n','')
        line = line.split(',')
        x = int(line[1])
        y = int(line[0])
        if i <= 1023:
            maze[x,y] = 1
        else:
            next_bits.append((x,y))
        i+=1
        
    
for bit in next_bits:
    print(bit)    
    maze[bit] = 1
    x = 0
    y = 0 
    visited = {}
    nums = queue.Queue()
    nums.put((0,x,y,''))
    while (x != 70 or y != 70) and nums:
        s,x,y,d = nums.get()
        if f"{x,y}" not in visited:
            visited[f"{x,y}"] = 1
            for j in ["<",">","^","v"]:
                res = valid_move(maze,s,x,y,j,d)
                if res:
                    nums.put(res)
    if not nums:
        print(bit)
        break