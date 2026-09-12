from collections import Counter, defaultdict


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = Counter(nums)

        specials = [x for x in freq if freq[x] == 3]

        cnt = defaultdict(list)

        for i, x in enumerate(nums):
            cnt[x].append(i)

        if not specials:
            return 0

        ans = 0

        for num in specials:
            indices = cnt[num]

            if indices[-1] - indices[-2] == indices[-2] - indices[-3]:
                ans += 1

        return ans