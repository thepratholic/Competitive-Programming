class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = (10 ** 9) + 7
        l = m = r = 0

        ans = 0

        for x in nums:
            if x < a:
                ans += (m + r)
                l += 1

            elif x > b:
                r += 1

            else:
                ans += r
                m += 1

        return ans % MOD