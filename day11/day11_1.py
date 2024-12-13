import time

def make_stones_great_again(file,number_of_blinks):   
    for x in range(number_of_blinks):
        print(x)
        group = []
        for num in file:
            if num == '0':
                group.append("1")
            elif len(num) % 2 == 0:
                length = len(num)//2
                num_1 = num[0:length]
                num_2 = str(int(num[length:]))               
                group.append(num_1)
                group.append(num_2)
            else:
                group.append(str(int(num)*2024))
        file = group
    return file                

start = time.time()
with open("data.txt",'r') as file:
    file = file.read()
    file = file.strip().split()
    print(len(make_stones_great_again(file,40)))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms") 