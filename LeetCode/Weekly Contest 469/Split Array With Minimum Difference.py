from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        mini = float('inf')
        n = len(nums)

        pre = [0] * n
        suff = [0] * n

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]


        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] + nums[i]


        inc = [False] * n
        inc[0] = True
        for i in range(1, n):
            if nums[i] > nums[i - 1] and inc[i - 1]:
                inc[i] = True

        dec = [False] * n
        dec[n - 1] = True
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1] and dec[i + 1]:
                dec[i] = True


        for i in range(n - 1):
            if inc[i] and dec[i + 1]:
                mini = min(mini, abs(pre[i] - suff[i + 1]))

        return mini if mini != float('inf') else -1