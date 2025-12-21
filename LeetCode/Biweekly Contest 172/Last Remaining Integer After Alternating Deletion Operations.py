class Solution:
    def lastInteger(self, n: int) -> int:
        a = 1
        d = 1
        turn = 0

        while True:
            sz = 1 + ((n - a) // d)
            if sz == 1:
                break

            if (turn & 1) and sz % 2 == 0:
                a += d

            d *= 2
            turn += 1

        return a