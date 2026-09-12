from collections import defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cnt = defaultdict(list)

        for i, x in enumerate(nums):
            cnt[x].append(i)

        ans = 0

        for indices in cnt.values():
            if len(indices) < 3: continue

            d = indices[1] - indices[0]

            if all(indices[i] - indices[i - 1] == d for i in range(2, len(indices))):
                ans += 1

        return ans