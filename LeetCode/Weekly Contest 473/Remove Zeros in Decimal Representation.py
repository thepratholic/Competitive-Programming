class Solution:
    def removeZeros(self, n: int) -> int:
        ans = []

        while n > 0:
            ld = n % 10
            if ld != 0:
                ans.append(ld)
            n //= 10

        ans = ans[::-1]
        return int("".join(map(str, ans)))