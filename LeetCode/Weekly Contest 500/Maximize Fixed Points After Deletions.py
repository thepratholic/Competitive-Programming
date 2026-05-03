from bisect import bisect_left


class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        pairs = []

        for i, x in enumerate(nums):
            if i >= x:
                pairs.append((i - x, x)) # (deletions on left, element)

        pairs.sort() # deletions can only be done in increasing fashion, can't undo and for same operations, take, smaller element

        lis = []
        for _, x in pairs:
            idx = bisect_left(lis, x)

            if idx == len(lis):
                lis.append(x)

            else:
                lis[idx] = x

        return len(lis)