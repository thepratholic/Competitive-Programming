from collections import defaultdict


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        ans = defaultdict(list)

        for idx, (x, y, r) in enumerate(drones):
            diff = abs(y - target[1]) + abs(x - target[0])

            if diff <= r:
                ans[diff].append(idx)


        if not ans:
            return -1

        else:
            mn = min(ans.keys())
            return min(ans[mn])