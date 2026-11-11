import sys
import math
from collections import deque, defaultdict, Counter
from itertools import combinations, permutations, accumulate, product

def input():
    return sys.stdin.readline().rstrip('\n')

def solve():
    n = int(input())

    v = []
    for _ in range(n):
        x, y = map(int, input().split())

        v.append((x, y))

    cnt = 0

    for i in range(n):
        x, y = v[i]
        l, r, u, d = False, False, False, False
        for j in range(n):
            x2, y2 = v[j]

            if x == x2:
                if y < y2: u = True
                elif y > y2: d = True
            elif y == y2:
                if x < x2: r = True
                elif x > x2: l = True

        if u == d == l == r == True: cnt += 1

    print(cnt)

def main():
    # t = int(input())
    # for _ in range(t):
    solve()

if __name__ == '__main__':
    main()