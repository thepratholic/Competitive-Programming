import sys, io, os
import math
import bisect
import heapq
import string
import re
from decimal import *
from random import randrange, choice, shuffle
from types import GeneratorType
from collections import defaultdict, Counter, deque

input = sys.stdin.readline

def I(): return input()
def II(): return int(input())
def MII(): return map(int, input().split())
def LI(): return list(input().split())
def LII(): return list(map(int, input().split()))
def GMI(): return map(lambda x: int(x) - 1, input().split())
def LGMI(): return list(map(lambda x: int(x) - 1, input().split()))
def WRITE(out): return print('\n'.join(map(str, out)))
def WS(out): return print(' '.join(map(str, out)))
def WNS(out): return print(''.join(map(str, out)))
def WSNOPRINT(out): return ''.join(map(str, out))

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


#@bootstrap
def solve():
    # Your solution here
    n, m, k = MII()
    total = n * m
    ans = 0

    for c in range(1, m):
        p1 = n * c
        p2 = n * (m - c)

        if p1 >= k:
            ans = max(ans, p2)

        if p2 >= k:
            ans = max(ans, p1)

    for r in range(1, n):
        p1 =  r * m
        p2 = (n - r) * m

        if p1 >= k:
            ans = max(ans, p2)

        if p2 >= k:
            ans = max(ans, p1)

    if k == 0:
        ans = max(ans, total)

    if k > total:
        print(0)

    print(ans)

def main():
    for _ in range(II()):
        solve()
main()