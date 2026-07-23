import sys
import os
from sys import stdin, stdout
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *
from string import *
from decimal import *
from fractions import Fraction
import re

input = stdin.readline

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(0, 0)] * (4 * self.n) # (gcd, cnt) cnt is nothing but freq of gcd i.e free in problem stmt
        self.build(0, 0, self.n - 1, arr)

    def merge(self, left, right):
        g = gcd(left[0], right[0])
        cnt = 0

        if g == left[0]:
            cnt += left[1]

        if g == right[0]:
            cnt += right[1]

        return (g, cnt)

    def build(self, idx, l, r, arr):
        if l == r:
            self.tree[idx] = (arr[l], 1)
            return

        mid = (l + r) >> 1

        self.build(2 * idx + 1, l, mid, arr)
        self.build(2 * idx + 2, mid + 1, r, arr)

        self.tree[idx] = self.merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

    def query(self, i, l, r, start, end):
        if r < start or end < l:
            return (0, 0)

        if l >= start and r <= end:
            return self.tree[i]

        mid = (l + r) >> 1

        left = self.query(2 * i + 1, l, mid, start, end)
        right = self.query(2 * i + 2, mid + 1, r, start, end)

        return self.merge(left, right)

    def update(self, idx, l, r, u_idx, u_val):
        if l == r:
            self.tree[idx] = (u_val, 1)
            return

        mid = (l + r) >> 1

        if u_idx <= mid:
            self.update(2 * idx + 1, l, mid, u_idx, u_val)
        else:
            self.update(2 * idx + 2, mid + 1, r, u_idx, u_val)

        self.tree[idx] = self.merge(self.tree[2 * idx + 1], self.tree[2 * idx + 2])

def solve():
    # Write your solution here
    n = int(input())
    s = list(map(int, input().split()))

    seg = SegmentTree(s)

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())

        l -= 1
        r -= 1

        g, free = seg.query(0, 0, n - 1, l, r)

        print((r - l + 1) - free)


# t = int(input())
# for _ in range(t):
solve()