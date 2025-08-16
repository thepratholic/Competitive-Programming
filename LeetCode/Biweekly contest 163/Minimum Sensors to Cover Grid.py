import math


class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        block = 2 * k + 1
        rows = math.ceil(n / block)
        cols = math.ceil(m / block)
        return rows * cols