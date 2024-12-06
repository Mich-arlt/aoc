with open("data.txt",'r') as file:
    sum = 0
    for line in file:
    # for v in range(1):
    
        numbers =  line.split()
        # numbers = [20,19,17,17,15]
        error = False
        chance = True
        numbers = [int(item) for item in numbers]
        diff = 0
        for i in range(len(numbers)-1):
            diff += numbers[i] - numbers[i+1]
        # print(diff)
        # print(numbers)
        if diff < 0:
            line_sum = 0
            i = 0
            while i < len(numbers)-1:
                if ((numbers[i] - numbers[i+1]) in [-1,-2,-3]):
                    # print('t')
                    line_sum+=1
                    i+=1
                elif (numbers[i] - numbers[i+1]) not in [-1,-2,-3] and chance == True:
                    print('o')
                    if i == 0:
                        numbers.pop(i)
                    else:
                        numbers.pop(i+1)
                    # print(numbers)
                    i=0
                    chance = False
                    line_sum = 0
                else:
                    error = True
                    break
            if line_sum == len(numbers)-1: 
                    sum+=1
                    print(numbers,"k")
            elif line_sum == len(numbers)-2 and chance == False and error == False: 
                    sum+=1
                    print(line_sum,len(numbers)-1)
                    print(numbers,"k")
            # else:
            #     print(line_sum,len(numbers)-1)
            #     print(numbers)
            chance = True
            error = False         
        elif diff > 0:
            line_sum = 0
            i = 0
            while i < len(numbers)-1:
                if (numbers[i] - numbers[i+1]) in [1,2,3]:
                    # print('t')
                    line_sum+=1
                    i+=1
                elif (numbers[i] - numbers[i+1]) not in [1,2,3] and chance == True:
                    print("o")
                    if i == 0:
                        numbers.pop(i)
                    else:
                        numbers.pop(i+1)
                    # print(numbers)
                    i=0
                    chance = False
                    line_sum = 0
                else:
                    error = True
                    break   
            if line_sum == len(numbers)-1:
                    sum+=1
                    print(numbers)
            elif line_sum == len(numbers)-2 and chance == False and error == False:
                    print(line_sum,len(numbers)-1) 
                    sum+=1
                    print(numbers,"k")
            # else:
            #     print(line_sum,len(numbers)-1)
            #     print(numbers)   
            chance = True
            error = False         
                     
                  
        else:
            continue
print(sum)           
    