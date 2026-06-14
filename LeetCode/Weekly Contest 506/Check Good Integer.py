class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        tmp1 = n

        sq = 0
        sum = 0

        while n > 0:
            ld = n % 10
            sq += (ld * ld)
            sum += ld
            n //= 10

        return (sq - sum) >= 50