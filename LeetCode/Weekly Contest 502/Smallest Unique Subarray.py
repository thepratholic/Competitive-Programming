from typing import Counter, List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # got this hash idea from one problem, and this template is from github, to store any big subarray type into map
        
        b = 911382323
        m = 10 ** 18 + 3

        pref = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            pref[i + 1] = (pref[i] * b + nums[i] + 1) % m
            power[i + 1] = (power[i] * b) % m

        def f(l, r):
            return (pref[r + 1] - pref[l] * power[r - l + 1]) % m
        

        def check(mid):
            fr = Counter()

            for i in range(n - mid + 1):
                sub = f(i, i + mid - 1)
                fr[sub] += 1

            for v in fr.values():
                if v == 1:
                    return True

            return False
        
        low, high = 1, n
        ans = n

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans