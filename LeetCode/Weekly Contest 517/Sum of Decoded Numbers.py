class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = (10 ** 9) + 7
        n = len(nums)
        ans = 0

        def get(num, w):
            x = str(num)[:w]
            y = str(num)[w:]

            return int(x), int(y)       
                

        for x in nums:
            width_i = x % 10
            d_i = x // 10

            xi, yi = get(d_i, width_i)

            ans = (ans + pow(xi, yi, MOD)) % MOD

        return ans