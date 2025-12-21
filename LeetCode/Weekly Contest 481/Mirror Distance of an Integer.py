class Solution:
    def mirrorDistance(self, n: int) -> int:
        def rev(n):
            ans = 0
            while n > 0:
                ld = n % 10
                ans = ans * 10 + ld
                n //= 10

            return ans


        r = rev(n)

        return abs(n - r)