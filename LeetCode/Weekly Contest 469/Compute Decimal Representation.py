from typing import List


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:

        ans = []
        s = str(n)
        sz = len(s)
        for i, ch in enumerate(s):
            digit = int(ch)
            if digit != 0:  
                ans.append(digit * (10 ** (sz - i - 1)))

        return sorted(ans, reverse=True)