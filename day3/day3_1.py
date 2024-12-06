import re
with open("data.txt",'r', encoding="utf-8") as text:
    text = text.read()
    x = re.findall(r"mul\((\d+,\d+)\)", text)
    sum = 0
    for mul in x:
        print(mul)
        mul = mul.replace('mul(',"")
        mul = mul.replace(')',"")
        mul = mul.split(',')
        sum+= int(mul[0]) * int(mul[1])

print(sum)