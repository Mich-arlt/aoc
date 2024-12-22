import numpy as np
import heapq

def if_way_find_E(maze,x,y):
    if maze[x+1,y] =="E":
        return True
    elif maze[x-1,y] =="E":
        return True
    elif maze[x,y+1] =="E":
        return True
    elif maze[x,y-1] =="E":
        return True
    return False

def add_move_if_possible(maze,p,d):
    point = p.copy()
    if d == '>' and maze[point[2],point[3]+1] == '.':
        if d == point[1]:
            point[0]+=1
            point[3]+=1
        elif point[1] == '<':
            return None
        else:
            point[0]+=1001
            point[1]=d
            point[3]+=1
        return point
            
    elif d == '<' and maze[point[2],point[3]-1] == '.':
        if d == point[1]:
            point[0]+=1
            point[3]-=1
            
        elif point[1] == '>':
            return None
        else:
            point[0]+=1001
            point[1]=d
            point[3]-=1
        return point
            
    elif d == '^' and maze[point[2]-1,point[3]] == '.':
        if d == point[1]:
            point[0]+=1
            point[2]-=1  
        elif point[1] == 'v':
            return None
        else:
            point[0]+=1001
            point[1]=d
            point[2]-=1  
        return point
            
    elif d == 'v' and maze[point[2]+1,point[3]] == '.':
        if d == point[1]:
            point[0]+=1
            point[2]+=1  
            
        elif point[1] == '^':
            return None
        else:
            point[0]+=1001
            point[1]=d
            point[2]+=1
        return point 
    else:
        return None
    
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    length = len(lines)
    maze = np.array([list(line) for line in lines])
start = np.where(maze == "S")
x = start[0][0]
y = start[1][0]  
nums = []
heapq.heappush(nums,[1,">",x,y])

visited={}

add = [0,"",0,0]
while not if_way_find_E(maze,add[2],add[3]):
    add = heapq.heappop(nums)
    if f"{add[2],add[3]}" not in visited or visited[f"{add[2],add[3]}"] > add[0]:
        visited[f"{add[2],add[3]}"] = add[0]
        for j in ["^","v",">",'<']:
            p = add_move_if_possible(maze,add,j)
            if p:
                heapq.heappush(nums,p) 
           
min_points = add[0]
print(min_points)
