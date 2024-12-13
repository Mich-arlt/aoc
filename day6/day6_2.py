import numpy as np
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]


def find_guard_way(lab_map):
    guard = np.where(lab_map == '^')
    i=guard[0]
    j=guard[1]
    direction = "up"
    sum=[]
    while i <len(lines) and j<len(lines) and i != 0 and j !=0:
        if direction == "up":
            while lab_map[(i,j)] != "#":
                if (int(i),int(j)) not in sum:
                    sum.append((int(i),int(j)))
                i-=1
                if lab_map[(i+1,j)] != "#" and i == -1:
                        break
            else:
                direction = "right"
                i+=1
        if direction == "right":
            while lab_map[(i,j)] != "#":
                if (int(i),int(j)) not in sum:
                    sum.append((int(i),int(j)))
                j+=1
                if lab_map[(i,j-1)] != "#" and j == len(lines):
                    break
            else:
                direction = "down"
                j-=1
        if direction == "down":
            while lab_map[(i,j)] != "#":
                if (int(i),int(j)) not in sum:
                    sum.append((int(i),int(j)))
                i+=1
                if lab_map[(i-1,j)] != "#" and i == len(lines):
                        break
            else:
                direction = "left"
                i-=1
        if direction == "left":
            while lab_map[(i,j)] != "#":
                if (int(i),int(j)) not in sum:
                    sum.append((int(i),int(j)))
                j-=1
                if lab_map[(i,j+1)] != "#" and j == -1:
                        break
            else:
                direction = "up"
                j+=1
    return sum

def check_loop(lab_map):
    # print(lab_map)  
    guard = np.where(lab_map == '^')
    i=guard[0]
    j=guard[1]
    direction = "up"
    sum=[]
    while i <len(lines) and j<len(lines) and i != -1 and j !=-1:
        if direction == "up":
            while lab_map[(i,j)] != "#":
                i-=1
                # print(i)
                if lab_map[(i+1,j)] != "#" and i == -1:
                        break
            else:
                direction = "right"
                i+=1
                if f"{i},{j},{direction}" in sum:
                    return True
                else:
                    sum.append(f"{i},{j},{direction}")
                
        if direction == "right":
            while lab_map[(i,j)] != "#":
                j+=1
                if lab_map[(i,j-1)] != "#" and j == len(lines):
                    break
            else:
                direction = "down"
                j-=1
                if f"{i},{j},{direction}" in sum:
                    return True
                else:
                    sum.append(f"{i},{j},{direction}")
                
        if direction == "down":
            while lab_map[(i,j)] != "#":
                i+=1
                if lab_map[(i-1,j)] != "#" and i == len(lines):
                        break
            else:
                direction = "left"
                i-=1
                if f"{i},{j},{direction}" in sum:
                    return True
                else:
                    sum.append(f"{i},{j},{direction}")
                
        if direction == "left":
            while lab_map[(i,j)] != "#":
                j-=1
                if lab_map[(i,j+1)] != "#" and j == -1:
                        break
            else:
                direction = "up"
                j+=1
                if f"{i},{j},{direction}" in sum:
                    return True
                else:
                    sum.append(f"{i},{j},{direction}")
    
    return False

suma =0             
lab_map = np.array([list(line) for line in lines])
ways = find_guard_way(lab_map)
for way in ways:
        if lab_map[way] != "#" and lab_map[way] != "^":
            lab_map[way] = "#"
            if check_loop(lab_map):
                suma+=1
            lab_map[way] = "."
print(suma)