class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:

        cnt = 0
        cur = 0
        for i in range(n * n):
            if cur + w > maxWeight:
                break
            cur += w
            cnt += 1

        return cnt