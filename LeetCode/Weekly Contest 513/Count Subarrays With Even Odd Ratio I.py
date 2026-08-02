class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)

        ans = 0

        for i in range(n):
            e = 0
            o = 0

            for j in range(i, n):
                if nums[j] & 1:
                    o += 1

                else:
                    e += 1

                if o > 0 and e * b <= a * o:
                    ans += 1

        return ans