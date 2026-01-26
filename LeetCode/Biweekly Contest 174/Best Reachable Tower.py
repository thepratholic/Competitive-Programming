from typing import List


class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        n = len(towers)
        reachable = []

        for x, y, q in towers:
            if abs(center[0] - x) + abs(center[1] - y) <= radius:
                reachable.append([x, y, q])

        if not reachable:
            return [-1, -1]

        reachable = sorted(reachable, key = lambda x : (-x[2], x[0], x[1]))

        return [reachable[0][0], reachable[0][1]]