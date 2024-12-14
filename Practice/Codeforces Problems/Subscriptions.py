import math
# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())

    incurrence = math.ceil(n/6)
    print(incurrence * x)