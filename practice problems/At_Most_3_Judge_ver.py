import sys
from collections import *
# sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0

    if min(a) > w:
        print(0)
        return
    

    seen = [False] * (w + 1)

    for i in range(n):
        if a[i] > w:
            break

        seen[a[i]] = True

        for j in range(i + 1, n):
            s2 = a[i] + a[j]

            if s2 > w:
                break

            seen[s2] = True

            for k in range(j + 1, n):
                s3 = s2 + a[k]

                if s3 > w:
                    break

                seen[s3] = True

    print(sum(seen))

t = 1
for _ in range(t):
    solve()