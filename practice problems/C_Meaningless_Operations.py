from collections import *
import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def solve():
    a = int(input())

    if (a & (a + 1)) != 0:
        k = a.bit_length()
        print((1 << k) - 1)
        return

    d = 2
    while d * d <= a:
        if a % d == 0:
            print(a // d)
            return
        d += 1

    print(1)
    

t = int(input())
for _ in range(t):
    solve()