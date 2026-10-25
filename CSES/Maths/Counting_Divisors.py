import sys
from math import sqrt
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    mx = max(nums)
    divs = [0] * (mx + 1)

    for i in range(1, mx + 1):
        for j in range(i, mx + 1, i):
            divs[j] += 1

    for x in nums:
        print(divs[x])

t = 1
for _ in range(t):
    solve()