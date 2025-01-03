import functools

@functools.cache
def count_ways(pattern:str):
    if not pattern:
        return 1
    ways = 0
    for towel in towels:
        if pattern.startswith(towel):
            ways+=count_ways(pattern[len(towel):])
    return ways

with open("data.txt", 'r') as file:
    lines = file.readlines()
    towels = lines[0].strip().split(", ")
    patterns = [line.strip() for line in lines[2:]]

result = 0
for pattern in patterns:
    result+=count_ways(pattern)

print(result)