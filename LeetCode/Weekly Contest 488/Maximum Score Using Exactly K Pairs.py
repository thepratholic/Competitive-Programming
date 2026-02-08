from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m = len(nums1), len(nums2)
        NEG_INF = float('-inf')

        dp = [[[NEG_INF] * (k + 1) for _ in range(m)] for _ in range(n)]
        vis = [[[False] * (k + 1) for _ in range(m)] for __ in range(n)]

        def f(i, j, kk):
            if kk == 0:
                return 0

            if i >= n or j >= m:
                return NEG_INF

            if vis[i][j][kk]:
                return dp[i][j][kk]

            vis[i][j][kk] = True

            take = f(i + 1, j + 1, kk - 1)
            if take != NEG_INF:
                take += (nums1[i] * nums2[j])

            skip1 = f(i + 1, j, kk)
            skip2 = f(i, j + 1, kk)

            dp[i][j][kk] = max(take, skip1, skip2)
            return dp[i][j][kk]

        return f(0, 0, k)