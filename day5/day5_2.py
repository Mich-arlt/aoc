with open("rules.txt",'r') as file:
    rules = []
    for line in file:
        line = line.replace('\n','')
        rules.append(line)
with open("data.txt",'r') as file:
    all_updates = []
    for line in file:
        line = line.replace('\n','')
        update = line.split(',')
        all_updates.append(update)
        
def check_update(update):
    for i in range(len(update)-1):
        for j in range(i+1,len(update)):
            if f"{update[i]}"+"|"+f"{update[j]}" not in rules:
                return True
    return False

def fix_update(update):
    for i in range(len(update)-1):
        for j in range(i+1,len(update)):
            if f"{update[i]}"+"|"+f"{update[j]}" not in rules:
                temp = update[i]
                update[i] = update[j]
                update[j] = temp
    mid = int((len(update))/2)
    return int(update[mid])
                

suma = 0 
for update in all_updates:
    if check_update(update):
        suma+=fix_update(update)
print(suma)       
    
    
#dictem lepiej bo wyszukujesz po kluczu zasady