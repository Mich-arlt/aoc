import re
with open("data.txt",'r', encoding="utf-8") as text:
    text = text.read()
    x = re.findall(r"mul\(\d+,\d+\)|do(?:n't)?\(\)", text)
    print(x)
    sum = 0
    pas = True 
    for mul in x:
        if mul == "don't()":
            pas = False
        elif mul =='do()':
            pas = True
        elif pas:
            mul = mul.replace('mul(',"")
            mul = mul.replace(')',"")
            mul = mul.split(',')
            sum+= int(mul[0]) * int(mul[1])

print(sum)