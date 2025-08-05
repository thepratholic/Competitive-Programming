from typing import List


class Solution:
    def earliestFinishTime(self, ls: List[int], ld: List[int], ws: List[int], wd: List[int]) -> int:
        n = len(ls)
        m = len(ws)

        enda = float('inf')
        for i in range(n):
            enda = min(enda, ld[i] + ls[i])

        endb = float('inf')
        for i in range(m):
            endb = min(endb, ws[i] + wd[i])

        pa = float('inf') # try land -> water
        for i in range(m):
            start = max(enda, ws[i])
            pa = min(pa, start + wd[i])

        pb = float('inf') # try water -> land
        for i in range(n):
            start = max(endb, ls[i])
            pb = min(pb, start + ld[i])

        return min(pa, pb)