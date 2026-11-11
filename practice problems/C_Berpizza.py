import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    q = int(input())

    max_heap = []
    q_ = deque()
    vis = set()
    index = 1
    while q:
        x = list(map(int, input().split()))

        if x[0] == 1:
            money = x[1]
            heappush(max_heap, (-money, index))
            q_.append((money, index))
            index += 1

        elif x[0] == 2:
            while q_ and q_[0][1] in vis:
                q_.popleft()

            if q_:
                first, arrival = q_.popleft()
                vis.add(arrival)
                print(arrival, end=" ")

        else:
            while max_heap and max_heap[0][1] in vis:
                heappop(max_heap)

            if max_heap:
                money, arrival = heappop(max_heap)
                money = -money
                vis.add(arrival)
                print(arrival, end=" ")

        q -= 1



if __name__ == '__main__':
    t = 1
    for _ in range(t):
        solve()