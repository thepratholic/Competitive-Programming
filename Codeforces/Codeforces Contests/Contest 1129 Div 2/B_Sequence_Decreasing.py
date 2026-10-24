import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    m = min(a)

    print(n if m <= n - 1 else 0)

t = int(input())
for _ in range(t):
    solve()