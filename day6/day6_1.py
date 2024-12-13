import numpy as np
import math
with open("data.txt",'r') as file:
    lines = [line.strip() for line in file.readlines()]
    lab_map = np.array([list(line) for line in lines])
    guard = np.where(lab_map == '^')
    print(len(lines))
    i=guard[0]
    j=guard[1]
    direction = "up"
    sum=[]
    while i <len(lines) and j<len(lines) and i != 0 and j !=0:
        if direction == "up":
            while lab_map[(i,j)] != "#":
                sum.append(f"{int(i)},{int(j)}")
                i-=1
                if lab_map[(i+1,j)] != "#" and i == -1:
                        break
            else:
                direction = "right"
                i+=1
        if direction == "right":
            while lab_map[(i,j)] != "#":
                sum.append(f"{int(i)},{int(j)}")
                j+=1
                if lab_map[(i,j-1)] != "#" and j == len(lines):
                    break
            else:
                direction = "down"
                j-=1
        if direction == "down":
            while lab_map[(i,j)] != "#":
                sum.append(f"{int(i)},{int(j)}")
                i+=1
                if lab_map[(i-1,j)] != "#" and i == len(lines):
                        break
            else:
                direction = "left"
                i-=1
        if direction == "left":
            while lab_map[(i,j)] != "#":
                sum.append(f"{int(i)},{int(j)}")
                j-=1
                if lab_map[(i,j+1)] != "#" and j == -1:
                        break
            else:
                direction = "up"
                j+=1
values, counts = np.unique(sum, return_counts=True)               
print(len(counts))