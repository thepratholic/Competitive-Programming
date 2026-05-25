class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        ans = float('inf')

        def cost(r, t):
            d = abs(r - t)
            return min(d, k - d)

        for x in range(k):
            for y in range(k):

                if x == y: continue

                ops = 0

                for i, val in enumerate(nums):

                    rem = val % k

                    if i & 1:
                        ops += cost(rem, y)
                    else:
                        ops += cost(rem, x)


                ans = min(ans, ops)

        return ans
                    