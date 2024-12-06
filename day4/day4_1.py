import math

def get_diagonal(text):
    length = int(math.sqrt(len(text.replace('\n',''))))
    diagonals=[]
    word=''
    text = text.replace('\n','')
    for i in range(length):
        word+=text[i]
        for j in range(1,i+1):           
            word+=text[i+(length-1)*j]
        diagonals.append(word)
        word =''


    return diagonals

def get_all_diagonal(text):
    diagonals = []
    diagonals.extend(get_diagonal(text)) 
    diagonals.extend(get_diagonal(text[::-1]))
    diagonals.pop(len(diagonals)-1) 
    rev = "\n".join(linia[::-1] for linia in text.splitlines())
    diagonals.extend(get_diagonal(rev)) 
    diagonals.extend(get_diagonal(rev[::-1]))
    diagonals.pop(len(diagonals)-1)
    return diagonals

def get_all_xmas(text:str):
    sum = 0
    sum+=text.count('XMAS')
    sum+=text.count('SAMX')
    wiersze = text.splitlines()
    obr_text = "\n".join("".join(wiersz[i] for wiersz in wiersze) for i in range(len(wiersze[0])))
    sum+=obr_text.count('XMAS')
    sum+=obr_text.count('SAMX')
    diagonals = get_all_diagonal(text)
    for diag in diagonals:
        sum+=diag.count('XMAS')
        sum+=diag.count('SAMX')
    return sum

with open("data.txt",'r') as text:
    text = text.read()
    
    print(get_all_xmas(text))