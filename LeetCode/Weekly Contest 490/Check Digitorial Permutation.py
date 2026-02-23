from math import factorial


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:

        sum = 0
        num = n

        while num > 0:
            ld = num % 10
            num //= 10

            sum += factorial(ld)

        return sorted(str(sum)) == sorted(str(n))