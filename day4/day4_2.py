import regex as re
import math
with open("data.txt",'r') as text:
    suma = 0
    text = text.read()
    text = text.replace('\n','0')
    length = int(math.sqrt(len(text)))
    pattern1 = r'M[A-Za-z]S.{' + str(length-1) + '}A.{' + str(length-1) + '}M[A-Za-z]S'
    matches1 = re.findall(pattern1, text,overlapped=True)
    
    suma += len(matches1)
    pattern2 = r'S[A-Za-z]S.{' + str(length-1) + '}A.{' + str(length-1) + '}M[A-Za-z]M'
    matches2 = re.findall(pattern2, text,overlapped=True)
    suma += len(matches2)
    pattern3 = r'M[A-Za-z]M.{' + str(length-1) + '}A.{' + str(length-1) + '}S[A-Za-z]S'
    matches3 = re.findall(pattern3, text,overlapped=True)
    suma += len(matches3)
    
    pattern4 = r'S[A-Za-z]M.{' + str(length-1) + '}A.{' + str(length-1) + '}S[A-Za-z]M'
    matches4 = re.findall(pattern4, text,overlapped=True)
    suma += len(matches4)
    
    print(suma)