class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = str(n)

        s = 0
        p = 1
        for i in n:
            s += int(i)
            p *= int(i)

        if int(n) % (p + s) == 0:
            return True
        else:
            return False
