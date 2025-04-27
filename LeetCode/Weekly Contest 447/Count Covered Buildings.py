from collections import defaultdict
import bisect
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        s = {(x, y) for x, y in buildings}
        
        rows = defaultdict(list)
        cols = defaultdict(list)
        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)
        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()
        
        covered = 0
        for x, y in buildings:
            ys = rows[x]
            xs = cols[y]
            
            i = bisect.bisect_left(ys, y)
            has_left  = (i > 0)
            has_right = (i < len(ys) - 1)
            
            j = bisect.bisect_left(xs, x)
            has_up    = (j > 0)
            has_down  = (j < len(xs) - 1)
            
            if has_left and has_right and has_up and has_down:
                covered += 1
        
        return covered
