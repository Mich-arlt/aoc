import numpy as np


def get_gps(m):
   boxes = np.where(m=="O")
   result = 0
   for i in range(len(boxes[0])):
        result+= boxes[0][i]*100 + boxes[1][i]  
   return result

def get_robot_work(ware_house,m,position,l):
    w =ware_house
    x = position[0][0]
    y = position[1][0]
    for move in m:
        if move == ">":
            if w[x,y+1] == ".":
                w[x,y+1] = "@"
                w[x,y] = "."
                y=y+1
            elif w[x,y+1] == "O":
                for i in range(y,l-1):   
                    if w[x,i] == ".":
                        w[x,i] = "O"
                        w[x,y+1] = "@"
                        w[x,y] = "."                             
                        y=y+1
                        break    
                    elif w[x,i] == "#":
                        break
            
        if move == "<":
            if w[x,y-1] == ".":
                w[x,y-1] = "@"
                w[x,y] ="."
                y=y-1
            elif w[x,y-1] == "O":
                for i in range(y-1,-1,-1):     
                    if w[x,i] == ".":
                        w[x,i] = "O"
                        w[x,y-1] = "@"
                        w[x,y] = "."
                        y=y-1
                        break    
                    elif w[x,i] == "#":
                        break
            
        if move == "v":
            if w[x+1,y] == ".":
                w[x+1,y] = "@"
                w[x,y] ="."
                x=x+1
            elif w[x+1,y] == "O":
                for i in range(x,l-1):     
                    if w[i,y] == ".":
                        w[i,y] = "O"
                        w[x+1,y] = "@"
                        w[x,y] = "."
                        x=x+1
                        break    
                    elif w[i,y] == "#":
                        break
            
        if move == "^":
            if w[x-1,y] == ".":
                w[x-1,y] = "@"
                w[x,y] = "."
                x = x-1
            elif w[x-1,y] == "O":
                for i in range(x-1,-1,-1):     
                    if w[i,y] == ".":
                        w[i,y] = "O"
                        w[x-1,y] = "@"
                        w[x,y] = "."
                        x=x-1
                        break    
                    elif w[i,y] == "#":
                        break
    return x,y,w








with open("data_warehouse.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    length = len(lines)
    warehouse = np.array([list(line) for line in lines])
    
with open("data_movement.txt") as file:
    move = file.read()
robot = np.where(warehouse == "@")

x,y,w = get_robot_work(warehouse,move,robot,length)
print(get_gps(w))