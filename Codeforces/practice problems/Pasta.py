import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    for i in range(m):
        need = b[i]

        ok = False

        for j in range(n):
            if a[j] == need:
                ok = True
                a[j] = -1
                break

        if not ok:
            print("No")
            return

    print("Yes")

t = 1
for _ in range(t):
    solve()