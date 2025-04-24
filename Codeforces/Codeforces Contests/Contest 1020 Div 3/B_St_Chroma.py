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

""" Was confused by the problem statement, specifically the movement.
ONE MOVE continues until one of the two conditions given are met. (Gnome meets candy or right most col)
A MOVE != All dwarves move one unit to the right """

#@bootstrap
def solve():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        res = []

        for i in range(x - 1, -1, -1):
            res.append(i)
        
        for i in range(n - 1, x, -1):
            res.append(i)
        
        res.append(x)

        print(' '.join(map(str, res)))


def main():
    solve()

main()