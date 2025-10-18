from collections import defaultdict
from typing import List


class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 2:
            return 0

        distance = [[0] * n for _ in range(n)]
        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                cur_dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distance[i][j] = distance[j][i] = cur_dist
                maxi = max(maxi, cur_dist)


        def can_group(d):
            graph = defaultdict(list)

            for i in range(n):
                for j in range(i + 1, n):
                    if distance[i][j] < d:
                        graph[i].append(j)
                        graph[j].append(i)

                    
            color = [-1] * n

            def dfs(node, col):
                color[node] = col

                for adjNode in graph[node]:
                    if color[adjNode] == -1:
                        if not dfs(adjNode, col ^ 1):
                            return False

                    elif color[node] == color[adjNode]:
                        return False

                return True


            for i in range(n):
                if color[i] == -1:
                    if not dfs(i, 0):
                        return False

            return True

        ans = -1
        low, high = 0, maxi
        while low <= high:
            mid = (low + high) >> 1

            if can_group(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans