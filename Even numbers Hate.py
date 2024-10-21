import math
for _ in range(int(input())):
    n = int(input())
    array = [*map(int, input().split())]
    counto =0
    counte =0
    for i in array:
        if i % 2 == 0:
            counte += 1
        else:
            counto += 1
    if counte == n:
        print(0)
    else:
        ans = math.ceil(counto/2) + counte
        print(ans)
