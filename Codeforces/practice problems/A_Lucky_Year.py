from sys import stdin
from collections import *

input = stdin.readline

def solve():
    n = int(input())

    nn = str(n)

    if len(nn) == 1:
        print(1)
        return

    nxt = int(str(int(nn[0]) + 1) + '0' * (len(nn) - 1))


    print(nxt - n)


t = 1
# t = int(input())
for _ in range(t):
    solve()