from sortedcontainers import SortedList


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)

        tot = n * (n + 1) // 2
        non = 0

        if k == 0:
            return tot

        pref = 0
        sl = SortedList([0])

        for x in nums:
            pref += x

            l = pref - goal - k
            r = pref - goal + k

            left = sl.bisect_right(l)
            right = sl.bisect_left(r)

            non += right - left

            sl.add(pref)

        return tot - non