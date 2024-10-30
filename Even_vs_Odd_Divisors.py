# cook your dish here
import math
t = int(input())
for _ in range(t):
    n = int(input())
    odd_divisors, even_divisors = 0, 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            if i % 2 == 0:
                even_divisors += 1
            else:
                odd_divisors += 1
            
            # Check corresponding divisor n // i if it's different from i
            if i != n // i:
                if (n // i) % 2 == 0:
                    even_divisors += 1
                else:
                    odd_divisors += 1
            
            
    if even_divisors > odd_divisors:
        print(1)
    if odd_divisors == even_divisors:
        print(0)
    if odd_divisors > even_divisors:
        print(-1)