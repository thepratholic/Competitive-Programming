import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    # n = int(input())
    a, b, c = map(int, input().split())
    ans = [0, 0, 0]

    if b % 2 == c % 2:
        ans[0] = 1

    if a % 2 == c % 2:
        ans[1] = 1

    if a % 2 == b % 2:
        ans[2] = 1

    print(*ans)

t = int(input())
for _ in range(t):
    solve()