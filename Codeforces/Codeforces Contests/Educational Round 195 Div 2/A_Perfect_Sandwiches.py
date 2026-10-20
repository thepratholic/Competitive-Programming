from sys import stdin
from collections import *

input = stdin.readline

def solve():
    a, b = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()

    if b >= a:
        print(-1)
        return

    print(min(b, a - b))
    

t = int(input())
for _ in range(t):
    solve()