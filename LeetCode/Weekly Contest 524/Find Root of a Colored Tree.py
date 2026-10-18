class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        n = len(colors)
        nxt = {'R' : 'B', 'B' : 'W', 'W' : 'R'}

        indeg = [0] * n
        deg = [0] * n

        for u, v in edges:
            deg[u] += 1
            deg[v] += 1

            if nxt[colors[u]] == colors[v]:
                indeg[v] += 1

            elif nxt[colors[v]] == colors[u]:
                indeg[u] += 1

            else:
                return -1

        root = -1

        for node in range(n):
            if indeg[node] == 0: # might be the root
                if root != -1:
                    return -1

                root = node

            elif indeg[node] != 1:
                return -1

        if root == -1 or deg[root] > 2:
            return -1

        return root