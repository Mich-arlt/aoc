import functools
import time

def make_stone_great_again(stones):
    new_stones = {}
    
    for key,val in stones.items():
        if key == "0":
            new_stones["1"] = new_stones.get("1", 0) + val
        elif len(key) % 2 == 0:
            length = len(key)//2
            num_1 = key[0:length]
            num_2 = f"{int(key[length:])}"
            new_stones[num_1] = new_stones.get(num_1, 0) + val
            new_stones[num_2] = new_stones.get(num_2, 0) + val
        else:
            new_stones[str((int(key)*2024))] = new_stones.get(str((int(key)*2024)), 0) + val
               
    return new_stones


start = time.time()
with open("data.txt",'r') as file:
    file = file.read()
    file = file.strip().split()
    stones ={}
    for num in file:
        stones[num] = 1
        
    for _ in range(75):
        stones = make_stone_great_again(stones)
    result = 0
    
print(sum(stones.values()))
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")   