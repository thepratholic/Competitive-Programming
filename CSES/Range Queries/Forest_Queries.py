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
    n, q = map(int, input().split())
    forest = [''] 

    for _ in range(n):
        forest.append(' ' + input())

    ps = [[0] * (n + 1) for _ in range(n + 1)]
     
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            tree = 1 if forest[i][j] == '*' else 0
            ps[i][j] = tree + ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]

    for _ in range(q):
        y1, x1, y2, x2 = map(int, input().split())
        result = ps[y2][x2] - ps[y1-1][x2] - ps[y2][x1-1] + ps[y1-1][x1-1]
        print(result)



def main():
    # for _ in range(II()):
        solve()
main()