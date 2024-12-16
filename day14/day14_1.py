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

def get_safety_factor(result,h,w):
    res_lu =0
    res_pu =0
    res_ld =0
    res_pd =0
    h_mid = h//2
    w_mid = w//2
    
    for robot in result:
        if robot[0] < w_mid and robot[1] < h_mid:
            res_lu+=1
        if robot[0] < w_mid and robot[1] > h_mid:
            res_ld+=1
        if robot[0] > w_mid and robot[1] < h_mid:
            res_pu+=1
        if robot[0] > w_mid and robot[1] > h_mid:
            res_pd+=1
    return res_pd*res_ld*res_lu*res_pu


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
result = []
for _,val in input.items():
    p = val[0]
    v = val[1]
    result.append(get_robot_end(p,v,100,h,w))

print(get_safety_factor(result,h,w))