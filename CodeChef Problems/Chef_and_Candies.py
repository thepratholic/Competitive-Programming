# cook your dish here
import math as m 
for _ in range(int(input())):
    
    n, x = map(int, input().split())
    if n <= x: 
        print(0)
        continue
    if n > x:
        n -= x 
    
    ans = m.ceil(n / 4)
    print(ans)