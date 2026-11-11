import sys
import math
import bisect
import heapq
import itertools
from collections import deque, defaultdict, Counter
from fractions import Fraction

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def map_ints():
    return map(int, input().split())

def list_ints():
    return list(map_ints())

# Number Theory
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def modexp(a, b, m):
    res = 1
    a %= m
    while b:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

def sieve(n):
    primes = []
    is_prime = [True] * (n + 1)
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

# Graph Algorithms
def bfs(graph, start):
    queue = deque([start])
    visited = set([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def dfs(graph, node, visited):
    stack = [node]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            stack.extend(graph[v])

# Disjoint Set Union (DSU)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rank[xr] < self.rank[yr]:
                xr, yr = yr, xr
            self.parent[yr] = xr
            if self.rank[xr] == self.rank[yr]:
                self.rank[xr] += 1

# Binary Search
def lower_bound(arr, x):
    return bisect.bisect_left(arr, x)

def upper_bound(arr, x):
    return bisect.bisect_right(arr, x)

# Kadane's Algorithm (Maximum Subarray Sum)
def max_subarray_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def min_subarray_sum(arr):
    min_sum = float('inf')
    curr_sum = 0
    for num in arr:
        curr_sum = min(num, curr_sum + num)
        min_sum = min(min_sum, curr_sum)
    return min_sum

# Prefix Sum
def prefix_sum(arr):
    psum = [0]
    for num in arr:
        psum.append(psum[-1] + num)
    return psum

# prime or not
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, int(n**0.5) + 1, 2):
        if n % d == 0:
            return False
    return True


def main():
    t = int_input()
    for _ in range(t):
        a, b = map(int, input().split())

        rem = abs((a ** 2) - (b ** 2))


        if (a - b == 1) and isPrime(a + b):
            print("YES")
        else:
            print("NO")



if __name__ == '__main__':
    main()