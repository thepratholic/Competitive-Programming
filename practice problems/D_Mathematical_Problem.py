import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()

    if n == 2:
        print(int(s))
        return

    best = float('inf')
    for i in range(n - 1):
        terms = [int(c) for c in s[:i]] + [int(s[i : i + 2])] + [int(c) for c in s[i + 2:]]
        if 0 in terms:
            val = 0

        else:
            val = sum(x for x in terms if x > 1)
            if val == 0:
                val = 1

        best = min(best, val)

    print(best)

t = int(input())
for _ in range(t):
    solve()