class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [int(d) for d in str(n)]

        nums.sort()

        return nums[-1] * nums[-2]