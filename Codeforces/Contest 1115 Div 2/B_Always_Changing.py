import sys
from sys import stdin

input = stdin.readline

def solve():
    n = int(input())
    s = input().strip()

    if all(s[i] != s[i - 1] for i in range(1, n)):
        print(0)
        return

    z = s.count('0')
    o = n - z

    if abs(z - o) > 2:
        print(-1)
        return

    k = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            k += 1

    c0 = (k + (s[0] == '0')) // 2
    c1 = k - c0

    d = c0 - c1
    x = z - o

    dr = 0
    if x == 2:
        dr = 1 - d
    if x == -2:
        dr = d + 1
    if abs(x) == 1 and d == -x:
        dr = 1

    print(n - (k - dr))


t = int(input())
for _ in range(t):
    solve()