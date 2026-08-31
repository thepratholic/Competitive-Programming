from collections import defaultdict

class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        d = defaultdict(list)

        for i, x in enumerate(nums):
            d[x].append(i)

        ans = 0

        for k, lst in d.items():
            ok = True
            for i in range(1, len(lst)):
                if lst[i] - lst[i - 1] > 1:
                    ok = False
                    break

            if ok:
                ans += 1

        return ans