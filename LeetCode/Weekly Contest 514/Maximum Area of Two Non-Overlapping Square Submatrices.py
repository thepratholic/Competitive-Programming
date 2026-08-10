from typing import List


class Solution:
    def maxArea(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        pref = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            for c in range(n):
                pref[r + 1][c + 1] = mat[r][c] + pref[r + 1][c] + pref[r][c + 1] - pref[r][c]


        def check(k):
            min_r = m
            max_r = -1
            min_c = n
            max_c = -1

            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    total = pref[r + k][c + k] - pref[r][c + k] - pref[r + k][c] + pref[r][c]

                    if total != k * k:
                        continue

                    if min_r != m and (r - min_r >= k or c - min_c >= k or max_c - c >= k):
                        return True

                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)

            return False


        low = 1
        high = min(m, n)

        ans = 0

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans * ans