from math import gcd


class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for removed in range(-1, n):
            arr = []

            for i in range(n):
                if i != removed:
                    arr.append(nums[i])

            m = len(arr)
            if m <= 1: continue

            pref = [0] * m
            suf = [0] * m

            pref[0] = arr[0]

            for i in range(1, m):
                pref[i] = gcd(pref[i - 1], arr[i])

            suf[-1] = arr[-1]
            for i in range(m - 2, -1, -1):
                suf[i] = gcd(suf[i + 1], arr[i])

            cur = 0
            for i in range(m - 1):
                if pref[i] == suf[i + 1]:
                    cur += 1

            ans = max(ans, cur)

        return ans