# cook your dish here
import math as m
for _ in range(int(input())):

    n, x = map(int, input().split())

    incr = m.ceil(n / 6)

    print(incr * x)