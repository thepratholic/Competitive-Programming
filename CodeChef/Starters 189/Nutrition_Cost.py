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

def solve():
    n, c = MII()
    vitamins = LII()
    cost = LII()

    min_cost = {}
    for i in range(n):
        v = vitamins[i]
        if v not in min_cost:
            min_cost[v] = cost[i]
        else:
            min_cost[v] = min(min_cost[v], cost[i])

    vitamin_costs = sorted(min_cost.values())
    ans = 0
    total_cost = 0
    for i, vcost in enumerate(vitamin_costs):
        total_cost += vcost
        ans = max(ans, c * (i + 1) - total_cost)
    print(ans)

def main():
    for _ in range(II()):
        solve()
main()
