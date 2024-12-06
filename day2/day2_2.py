def check_line_with_bad_lvl(line,diff):
    for i in range(len(line)):
        temp_line = line[:i] + line[i+1:] 
        print(temp_line)
        if check_line(temp_line, diff):
            return True
    return False
    

def check_line(line,diff):
    i=0      
    line_sum = 0
    if diff == "up":
        while i < len(line)-1:
            if (line[i] - line[i+1])  in [-1,-2,-3]:
                line_sum +=1
            i+=1
    elif diff == "down":      
        while i < len(line)-1:
            if (line[i] - line[i+1]) in [1,2,3]:
                line_sum +=1
            i+=1 
    else:
        return False     
    if line_sum == len(line)-1: 
        return True
   


with open("data.txt",'r') as file:
    sum = 0
    for line in file:   
        numbers =  line.split()
        numbers = [int(item) for item in numbers]
        diff_plus = 0
        diff_minus = 0
        for i in range(len(numbers)-1):
            if numbers[i] - numbers[i+1] < 0: 
                diff_plus +=1
            elif numbers[i] - numbers[i+1] > 0:
                diff_minus +=1
            else:
                continue
        diff =''
        if diff_plus > diff_minus:
            diff = 'up'
        elif diff_plus < diff_minus:
            diff = 'down'
        if check_line(numbers,diff):
            sum+=1
        elif check_line_with_bad_lvl(numbers,diff):
            sum+=1
            
    
    