import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()

    t = []
    m = []

    for i in range(n):
        if s[i] == 'T':
            t.append(i)

        else:
            m.append(i)

    if len(t) != 2 * len(m):
        print("NO")
        return

    sz = len(m)

    for i in range(sz):
        if m[i] < t[i] or m[i] > t[i + sz]:
            print("NO")
            return

    print("YES")

# TC : O(n) + O(no of M)
# SC : O(n)

t = int(input())
for _ in range(t):
    solve()