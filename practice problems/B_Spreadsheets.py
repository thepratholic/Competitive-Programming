import re
import math
def getchar(s):
    a=[]
    while s>0:
        c = s%26 if s%26 else 26
        a.insert(0,c)
        s = (s-c)//26
    return "".join(chr(i+64) for i in a)
def getNumber(s):
    rs=0
    for i,c in enumerate(s[::-1]):
        v=ord(c)-64
        rs+= (26**i) * v
    return rs
n=int(input())
for _ in range(n):
    a=input()
    if re.match(r'^R\d+C\d+',a):
        ar=re.findall(r'\d+',a)
        print(getchar(int(ar[1]))+ar[0])
    else:
        st=re.findall(r'[A-Z]+',a)
        nt=re.findall(r'\d+',a)
        print(f"R{nt[0]}C{getNumber(st[0])}")