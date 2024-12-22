import numpy as np
import heapq

def if_way_find_E(maze,x,y):
    if maze[x+1,y] =="E":
        return (x+1,y)
    elif maze[x-1,y] =="E":
        return (x-1,y)
    elif maze[x,y+1] =="E":
        return (x,y+1)
    elif maze[x,y-1] =="E":
        return (x,y-1)
    return ""

def add_move_if_possible(maze,p,d):
    point = p.copy()
    x = point[2]
    y = point[3]
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
heapq.heappush(nums,[1,">",x,y,[],10])

same_points = {}
visited={}
min_points =100000
add = [0,"",0,0,[],10]

while nums:
    add = heapq.heappop(nums)
    
    if f"{add[2],add[3]}" not in visited or visited[f"{add[2],add[3]}"] > add[0]:
        visited[f"{add[2],add[3]}"] = add[0]
        for j in ["^","v",">",'<']:
            x = add[2]
            y = add[3]
            p = add_move_if_possible(maze,add,j)
            if p and p[0] < min_points:
                p[4] = p[4][:]
                p[4].append((x,y)) 
                heapq.heappush(nums,p)
    elif add[5]!=0:
        for j in ["^","v",">",'<']:
            x = add[2]
            y = add[3]
            
            p = add_move_if_possible(maze,add,j)
            if p and p[0] < min_points:
                p[4] = p[4][:]
                p[4].append((x,y))
                p[5]-=1 
                heapq.heappush(nums,p)
        
    elif f"{add[2],add[3]}" in visited and visited[f"{add[2],add[3]}"] == add[0]:
        same_points[(add[2], add[3])] = same_points.get((add[2], add[3]), []) + (add[4]) 
    
    e = if_way_find_E(maze,add[2],add[3])
    if e != '' and add[0] <= min_points:
        add[4].append((add[2],add[3]))
        add[4].append(e)
        all_tiles = add[4]
        break
    
    
start = len(same_points)
end = 0
while start != end:
    start =  len(same_points)
    for key,val in same_points.items():
            if key in all_tiles:
                x_val = val[-2][0] - val[-1][0]
                y_val = val[-2][1] - val[-1][1]                
                key_index = all_tiles.index(key)
                x_path = all_tiles[key_index-1][0] - all_tiles[key_index][0]
                y_path = all_tiles[key_index-1][1] - all_tiles[key_index][1] 
                all_tiles.extend(val)
                same_points.pop(key)
                break
    end = len(same_points) 
print(len(set(all_tiles)))   

