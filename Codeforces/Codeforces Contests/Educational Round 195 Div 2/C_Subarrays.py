from sys import stdin
from collections import *

input = stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    # s = input().strip()

    p = [0] * (n + 1)

    for i in range(1, n + 1):
        p[i] = p[i - 1] + a[i - 1]

    cnt = 0
    f = [0] * k

    l = 0

    for r in range(1, n + 1):
        upto = r - k

        while l < upto:
            l += 1
            f[p[l - 1] % k] += 1

        cnt += f[p[r] % k]

    print(cnt)
    

t = int(input())
for _ in range(t):
    solve()