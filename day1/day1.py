data_l = []
data_r = []

index=0
with open("data.txt",'r') as file:
    for line in file:
        numbers = line.split()
        data_l.append(numbers[0])
        data_r.append(numbers[1])
data_l.sort()
data_r.sort()

sum = 0
for i in range(len(data_l)):
    sum+= abs(int(data_l[i]) - int(data_r[i]))
    
print(sum)
    
sum_2 = 0
app = 0 
for num in data_l:
    for id in data_r:
        if num == id:
            app+=1
    sum_2+= int(num) * app
    app = 0
        
print(sum_2)

    