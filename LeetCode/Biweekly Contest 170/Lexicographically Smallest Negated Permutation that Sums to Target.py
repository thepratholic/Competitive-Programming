from typing import List


class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        tot = n * (n + 1) // 2
        if abs(target) > tot or (tot + target) & 1:
            return []
        
        x = (tot + target) // 2
        rem = x
        pos = [False] * (n + 1)
        
        for i in range(n, 0, -1):
            S_prev = (i - 1) * i // 2
            if rem > S_prev:
                pos[i] = True
                rem -= i
        
        res = []
        for i in range(n, 0, -1):
            if not pos[i]:
                res.append(-i)
                
        for i in range(1, n + 1):
            if pos[i]:
                res.append(i)
        
        return res