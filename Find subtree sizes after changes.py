from collections import defaultdict
from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_tree = defaultdict(list)
        last_seen = {}

        for x in range(n):
            if x == 0:
                continue

            current = parent[x]
            while current != -1 and s[current] != s[x]:
                current = parent[current]

            if current != -1:
                new_tree[current].append(x)
            else:
                new_tree[parent[x]].append(x)

        answer = [0] * n

        def dfs(node):

            size = 1
            for child in new_tree[node]:
                size += dfs(child)
            answer[node] = size
            return size
        dfs(0)

        return answer