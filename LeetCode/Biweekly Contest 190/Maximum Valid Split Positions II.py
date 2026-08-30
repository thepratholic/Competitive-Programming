from math import gcd 

class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)

        def f(arr):
            m = len(arr)

            pref = [0] * m
            suf = [0] * m

            pref[0] = arr[0]
            for i in range(1, m):
                pref[i] = gcd(pref[i - 1], arr[i])

            suf[-1] = arr[-1]
            for i in range(m - 2, -1, -1):
                suf[i] = gcd(suf[i + 1], arr[i])

            ans = 0
            for i in range(m - 1):
                if pref[i] == suf[i + 1]:
                    ans += 1

            return ans

        # case 1 : remove nothing
        ans = f(nums)

        # 2 : remove nums[0]
        ans = max(ans, f(nums[1:]))

        # 3 : remove nums[-1]
        ans = max(ans, f(nums[:-1]))

        pref = [0] * n
        suf = [0] * n

        pref[0] = nums[0]
        for i in range(1, n):
            pref[i] = gcd(pref[i - 1], nums[i])

        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = gcd(suf[i + 1], nums[i])

        # 4 : remove any middle element and see
        cand = -1
        for i in range(1, n - 1):
            left = pref[i - 1]
            right = suf[i + 1]

            common = gcd(left, right)

            if common != gcd(common, nums[i]): # means nums[i] is reducing the gcd, worth removing
                cand = i
                break

        if cand != -1:
            ans = max(ans, f(nums[:cand] + nums[cand + 1:]))
        
        return ans