import math


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = sides

        if not (a + b > c and a + c > b and b + c > a):
            return []

        def angle(opp, x, y):
            val = (x * x + y * y - opp * opp) / (2 * x * y)
            val = max(-1, min(1, val)) # too confusing;
            return math.degrees(math.acos(val))

        a_ = angle(a, b, c)
        b_ = angle(b, a, c)
        c_ = angle(c, a, b)

        return sorted([a_, b_, c_])