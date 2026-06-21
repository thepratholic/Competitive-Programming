import sys
import math
import heapq
import bisect
from collections import deque, defaultdict, Counter

# ============================================================
#                       FAST I/O
# ============================================================
input = sys.stdin.readline

def read_int():
    return int(input())

def read_ints():
    return list(map(int, input().split()))

def read_str():
    return input().strip()

def read_strs():
    return input().split()

# Use this for output instead of multiple print() calls
out = []
def flush_output():
    sys.stdout.write('\n'.join(map(str, out)) + '\n')


# ============================================================
#                       CONSTANTS
# ============================================================
MOD = 10 ** 9 + 7
INF = float('inf')


# ============================================================
#                       MATH UTILITIES
# ============================================================
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def power(base, exp, mod=MOD):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def mod_inverse(a, mod=MOD):
    return power(a, mod - 2, mod)

def sieve(n):
    """Returns (list_of_primes, is_prime_boolean_array) up to n inclusive."""
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    primes = [i for i, p in enumerate(is_p) if p]
    return primes, is_p

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# ============================================================
#                  DSU / UNION-FIND (size-based)
# ============================================================
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


# ============================================================
#                       SEGMENT TREE
# ============================================================
class SegmentTree:
    """Generic iterative segment tree.
    Default: sum. Pass func=min / max for other use-cases (with proper default)."""
    def __init__(self, arr, func=lambda a, b: a + b, default=0):
        self.n = len(arr)
        self.func = func
        self.default = default
        self.tree = [default] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos >>= 1
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, l, r):
        """Range query on [l, r) -> half-open interval."""
        res = self.default
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


# ============================================================
#                       SPARSE TABLE
# ============================================================
class SparseTable:
    """Static range query (min/max/gcd) in O(1) after O(n log n) build."""
    def __init__(self, arr, func=min):
        self.n = len(arr)
        self.func = func
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        self.k = self.log[self.n] + 1 if self.n > 0 else 1
        self.table = [arr[:]] + [[0] * self.n for _ in range(self.k - 1)]
        for j in range(1, self.k):
            half = 1 << (j - 1)
            for i in range(self.n - (1 << j) + 1):
                self.table[j][i] = func(self.table[j - 1][i], self.table[j - 1][i + half])

    def query(self, l, r):
        """Inclusive range query [l, r]."""
        j = self.log[r - l + 1]
        return self.func(self.table[j][l], self.table[j][r - (1 << j) + 1])


# ============================================================
#                           TRIE
# ============================================================
class TrieNode:
    __slots__ = ['children', 'is_end']
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find(prefix) is not None

    def _find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ============================================================
#                           GRAPH
# ============================================================
class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = defaultdict(list)  # u -> list of (v, weight)

    def add_edge(self, u, v, w=1):
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

    def bfs(self, start):
        visited = [False] * self.n
        dist = [INF] * self.n
        visited[start] = True
        dist[start] = 0
        q = deque([start])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, w in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    q.append(v)
        return order, dist

    def dfs(self, start):
        visited = [False] * self.n
        order = []
        stack = [start]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            order.append(u)
            for v, w in reversed(self.adj[u]):
                if not visited[v]:
                    stack.append(v)
        return order

    def dijkstra(self, start):
        dist = [INF] * self.n
        dist[start] = 0
        pq = [(0, start)]
        visited = [False] * self.n
        while pq:
            d, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

    def topological_sort(self):
        """Kahn's algorithm. Returns [] if graph has a cycle."""
        indegree = [0] * self.n
        for u in self.adj:
            for v, w in self.adj[u]:
                indegree[v] += 1
        q = deque([i for i in range(self.n) if indegree[i] == 0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v, w in self.adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return order if len(order) == self.n else []

    def kruskal_mst(self, edges):
        """edges: list of (weight, u, v). Returns (total_weight, mst_edges)."""
        dsu = DSU(self.n)
        total = 0
        mst_edges = []
        for w, u, v in sorted(edges):
            if dsu.union(u, v):
                total += w
                mst_edges.append((u, v, w))
        return total, mst_edges

    def prim_mst(self, start=0):
        visited = [False] * self.n
        pq = [(0, start)]
        total = 0
        while pq:
            w, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            total += w
            for v, wt in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (wt, v))
        return total

    def floyd_warshall(self):
        dist = [[INF] * self.n for _ in range(self.n)]
        for i in range(self.n):
            dist[i][i] = 0
        for u in self.adj:
            for v, w in self.adj[u]:
                dist[u][v] = min(dist[u][v], w)
        for k in range(self.n):
            dk = dist[k]
            for i in range(self.n):
                dik = dist[i][k]
                if dik == INF:
                    continue
                di = dist[i]
                for j in range(self.n):
                    if dik + dk[j] < di[j]:
                        di[j] = dik + dk[j]
        return dist


# ============================================================
#                  LCA (Binary Lifting on a tree)
# ============================================================
class LCA:
    """tree_adj: List[List[int]] -- plain unweighted adjacency list of a tree."""
    def __init__(self, n, tree_adj, root=0):
        self.n = n
        self.LOG = max(1, n.bit_length())
        self.depth = [0] * n
        self.up = [[0] * n for _ in range(self.LOG)]

        parent = [-1] * n
        visited = [False] * n
        visited[root] = True
        stack = [root]
        while stack:
            u = stack.pop()
            for v in tree_adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    self.depth[v] = self.depth[u] + 1
                    stack.append(v)

        for i in range(n):
            self.up[0][i] = parent[i] if parent[i] != -1 else i

        for k in range(1, self.LOG):
            for v in range(n):
                self.up[k][v] = self.up[k - 1][self.up[k - 1][v]]

    def query(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if (diff >> k) & 1:
                u = self.up[k][u]
        if u == v:
            return u
        for k in range(self.LOG - 1, -1, -1):
            if self.up[k][u] != self.up[k][v]:
                u = self.up[k][u]
                v = self.up[k][v]
        return self.up[0][u]


# ============================================================
#                     COMMON PATTERNS
# ============================================================
def kadane(arr):
    """Maximum subarray sum."""
    max_sum = cur_sum = arr[0]
    for x in arr[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

def binary_search(lo, hi, condition):
    """Finds smallest x in [lo, hi] for which condition(x) is True (monotonic)."""
    while lo < hi:
        mid = (lo + hi) // 2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def lower_bound(arr, x):
    return bisect.bisect_left(arr, x)

def upper_bound(arr, x):
    return bisect.bisect_right(arr, x)

def prefix_sum(arr):
    n = len(arr)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + arr[i]
    return pre

def prefix_xor(arr):
    n = len(arr)
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] ^ arr[i]
    return pre


# ============================================================
#                       MAIN STRUCTURE
# ============================================================
def solve():
    n, m = read_ints()

    

def main():
    t = 1
    # t = read_int()   # uncomment if multiple test cases
    for _ in range(t):
        solve()
    flush_output()

if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 6)
    main()
