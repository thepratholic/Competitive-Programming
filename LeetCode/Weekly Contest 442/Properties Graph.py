from collections import defaultdict
from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        
        sets = [set(row) for row in properties]

        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if len(sets[i] & sets[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()
        def dfs(node):
            stack = [node]
            while stack:
                cur = stack.pop()
                for neighbor in graph[cur]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        components = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components += 1

        return components