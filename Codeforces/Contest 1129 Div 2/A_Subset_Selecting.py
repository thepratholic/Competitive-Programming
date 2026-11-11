import sys
from collections import *
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = [0] * (n + 2)
    for x in a:
        cnt[x] += 1

    ans = 0
    pref = 0

    for v in range(n + 1):
        pref += cnt[v]
        
        if cnt[v] >= 1 and pref >= k * (v + 1):
            ans = v + 1
        else:
            break
    print(ans)


t = int(input())
for _ in range(t):
    solve()