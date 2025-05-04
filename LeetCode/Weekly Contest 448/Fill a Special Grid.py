from typing import List


class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def build(n, base=0):
            if n == 0:
                return [[base]]
            
            size = 2 ** (n - 1)
            offset = size * size
            
            q1 = build(n - 1, base)
            q2 = build(n - 1, base + offset)
            q3 = build(n - 1, base + 2 * offset)
            q4 = build(n - 1, base + 3 * offset)
            
            top = [q4[i] + q1[i] for i in range(size)]
            bottom = [q3[i] + q2[i] for i in range(size)]
            
            return top + bottom
        return build(N)
