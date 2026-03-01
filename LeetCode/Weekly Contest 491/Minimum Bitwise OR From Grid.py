from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans = (1 << 20) - 1
        for bit in range(19, -1, -1):
            wans = ans ^ (1 << bit) # we want this bit to be there in the final ans, basicaally 0
            pos = True

            for row in grid:
                sub = False

                for val in row:
                    if (val | wans) == wans:
                        sub = True

                if not sub:
                    pos = False

            if not pos:
                continue

            ans = wans

        return ans