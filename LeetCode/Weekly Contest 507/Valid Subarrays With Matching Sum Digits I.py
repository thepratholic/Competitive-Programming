class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)

        ans = 0
        x = str(x)

        for i in range(n):
            cur = 0

            for j in range(i, n):
                cur += nums[j]

                s = str(cur)
                if s[0] == x and s[-1] == x:
                    ans += 1


        return ans