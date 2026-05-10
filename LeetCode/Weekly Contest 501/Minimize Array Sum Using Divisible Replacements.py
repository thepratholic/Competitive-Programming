class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        mx = max(nums) + 1

        pre = [False] * (mx)

        for x in nums:
            pre[x] = True

        mn = list(range(mx))

        for v in range(1, mx):
            if pre[v]:
                for mult in range(v, mx, v):
                    mn[mult] = min(mn[mult], v)

        return sum(mn[x] for x in nums)