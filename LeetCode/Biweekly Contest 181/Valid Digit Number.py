class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        n = str(n)
        x = str(x)

        return x in n and n[0] != x