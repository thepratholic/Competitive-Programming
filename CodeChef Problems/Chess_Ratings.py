# cook your dish here
import math as m 
for _ in range(int(input())):
    
    x, y = map(int, input().split())
    
    print(m.ceil((y - x) / 8))