import heapq
import functools

@functools.cache
def valid_patern(towel, pattern):
    return pattern.startswith(towel)

with open("data.txt", 'r') as file:
    lines = file.readlines()
    towels = lines[0].strip().split(", ")
    patterns = [line.strip() for line in lines[1:]]

print(towels)
print(patterns)

result = 0
for pattern in patterns:
    correct_towels = []
    for t in towels:
        if pattern.__contains__(t):
            correct_towels.append(t)
    word = ""
    
    word_heap = []
    heapq.heappush(word_heap, (-len(word), word))
    valid_word = {}
    while word_heap :
        _, word = heapq.heappop(word_heap)
        for towel in correct_towels:
            new_word = word + towel
            if  valid_patern(new_word, pattern):
                valid_word[new_word] = 1
                heapq.heappush(word_heap, (-len(new_word), new_word))
    
        if word == pattern:
            print(word)
            result += 1

print(result)
