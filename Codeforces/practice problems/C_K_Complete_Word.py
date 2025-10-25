import sys
from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))

    def findUPar(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)
    
    def union(self, u, v):
        uu, uv = self.findUPar(u), self.findUPar(v)
        if uu == uv:
            return
        if self.size[uu] < self.size[uv]:
            self.parent[uu] = uv
            self.size[uv] += self.size[uu]
        else:
            self.parent[uv] = uu
            self.size[uu] += self.size[uv]

def solve():
    n, k = map(int, input().split())
    s = input().strip()

    dsu = DSU(n)

    for i in range(k):
        for j in range(i, n, k):
            dsu.union(i, j)

    for i in range(n):
        dsu.union(i, n - i - 1)

    groups = defaultdict(list)
    for i in range(n):
        parent = dsu.findUPar(i)
        groups[parent].append(i)

    ans = 0

    for idxs in groups.values():
        freq = [0] * 26
        maxi = 0
        for x in idxs:
            freq[ord(s[x]) - ord('a')] += 1
            maxi = max(maxi, freq[ord(s[x]) - ord('a')])
        ans += len(idxs) - maxi

    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
