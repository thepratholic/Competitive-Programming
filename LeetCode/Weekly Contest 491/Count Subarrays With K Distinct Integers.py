from typing import DefaultDict


class Solution:
    def countSubarrays(self, a: list[int], k: int, m: int) -> int:
        n = len(a)
        ans = 0

        r1, r2 = -1, -1
        count = 0
        freq1 = DefaultDict(int)
        freq2 = DefaultDict(int)

        for l in range(n):

            while r2 < n and len(freq1) < k + 1: # finding invalid index where distinct is equal to k + 1
                r2 += 1

                if r2 < n:
                    freq1[a[r2]] += 1

            while r1 < n and count < k: # finding first valid index where 'count' elements have >= m freq
                r1 += 1

                if r1 < n:
                    freq2[a[r1]] += 1
                    if freq2[a[r1]] == m:
                        count += 1

            if r1 < r2:
                ans += (r2 - r1)

            freq1[a[l]] -= 1
            if freq1[a[l]] == 0:
                del freq1[a[l]]

            freq2[a[l]] -= 1
            if freq2[a[l]] == m - 1:
                count -= 1

        return ans