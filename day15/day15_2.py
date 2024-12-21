import numpy as np


def get_gps(m):
   boxes = np.where(m=="[")
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
            elif w[x,y+1] == "[":
                for i in range(y,l-1):   
                    if w[x,i] == ".":
                        p = 0
                        for j in range(y+2,i+1):
                            if p % 2 == 0:
                                w[x,j] = "["
                            else:
                                w[x,j] = "]"
                            p+=1  
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
            elif w[x,y-1] == "]":
                for i in range(y-1,-1,-1):     
                    if w[x,i] == ".":
                        p = 0
                        for j in range(i,y-1):
                            if p % 2 == 0:
                                w[x,j] = "["
                            else:
                                w[x,j] = "]"
                            p+=1  
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
            elif w[x+1,y] in ['[',']']:
                if w[x+1,y] == "[":
                    boxes = [(x+1,y),(x+1,y+1)]
                else:
                    boxes = [(x+1,y),(x+1,y-1)]
                checked_boxes = []
                for i in range(x,l-1):
                   if "#" in boxes:
                        break
                   elif not boxes:
                       checked_boxes = list(dict.fromkeys(checked_boxes))
                       for b in range(len(checked_boxes)-1,-1,-1):
                           box = checked_boxes[b]
                           w[box[0]+1,box[1]] = w[box]
                           w[box] = "."
                       w[x+1,y] = "@"
                       w[x,y] = "."
                       x = x+1
                       break     
                   temp = []   
                   for box in boxes:
                       if w[box[0]+1,box[1]] in ['[',']']:
                            if w[box[0]+1,box[1]] == '[':
                                temp.append((box[0]+1,box[1]))
                                temp.append((box[0]+1,box[1]+1))
                            else:
                                temp.append((box[0]+1,box[1]))
                                temp.append((box[0]+1,box[1]-1))
                       elif w[box[0]+1,box[1]] == '#':
                           temp.append("#")                            
                   checked_boxes.extend(boxes)
                   boxes = temp
            
        if move == "^":
            if w[x-1,y] == ".":
                w[x-1,y] = "@"
                w[x,y] = "."
                x = x-1
            elif w[x-1,y] in ['[',']']:
                if w[x-1,y] == "[":
                    boxes = [(x-1,y),(x-1,y+1)]
                else:
                    boxes = [(x-1,y),(x-1,y-1)]
                checked_boxes = []
                for i in range(x-1,-1,-1):
                   if "#" in boxes:
                        break
                   elif not boxes:
                       checked_boxes = list(dict.fromkeys(checked_boxes))
                       for b in range(len(checked_boxes)-1,-1,-1):
                           box = checked_boxes[b]
                           w[box[0]-1,box[1]] = w[box]
                           w[box] = "."
                       w[x-1,y] = "@"
                       w[x,y] = "."
                       x = x-1
                       break     
                   temp = []   
                   for box in boxes:
                       if w[box[0]-1,box[1]] in ['[',']']:
                            if w[box[0]-1,box[1]] == '[':
                                temp.append((box[0]-1,box[1]))
                                temp.append((box[0]-1,box[1]+1))
                            else:
                                temp.append((box[0]-1,box[1]))
                                temp.append((box[0]-1,box[1]-1))
                       elif w[box[0]-1,box[1]] == '#':
                           temp.append("#")                            
                   checked_boxes.extend(boxes)
                   boxes = temp
                   
                    
    return x,y,w

def double_map(line):
    result =''
    for x in line:
        if x == "#":
            result+="##"
        elif x =="O":
            result+="[]"
        elif x =='.':
            result+='..'
        elif x =='@':
            result+='@.'    

    return result




with open("data_warehouse.txt",'r') as file:
    lines = [double_map(line.strip()) for line in file.readlines()]
    length = len(lines*2)
    warehouse = np.array([list(line) for line in lines])
    
with open("data_movement.txt") as file:
    move = file.read()
robot = np.where(warehouse == "@")

x,y,w = get_robot_work(warehouse,move,robot,length)
print(get_gps(w))