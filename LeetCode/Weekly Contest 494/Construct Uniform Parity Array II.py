class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        odd, even = 0, 0

        for x in nums1:
            if x & 1: odd += 1
            else:
                even += 1

        if (odd == n) or (odd == 0):
            return True

        mn = min(nums1)
        return True if mn & 1 else False