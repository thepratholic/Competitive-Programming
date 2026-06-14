from collections import defaultdict
from typing import List


class Solution:
    def getLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        for i in range(n):
            freq = defaultdict(int)
            c = defaultdict(int)

            for j in range(i, n):
                x = nums[j]

                if x in freq:
                    old = freq[x]
                    c[old] -= 1

                    if c[old] == 0:
                        del c[old]

                freq[x] += 1
                new = freq[x]
                c[new] += 1

                distinct = len(freq)
                sz = j - i + 1

                bal = False

                if distinct == 1:
                    bal = True

                elif sz == 1:
                    bal = True

                elif len(c) == 2:
                    f1, f2 = sorted(c.keys())
                    if f2 == 2 * f1:
                        bal = True

                if bal:
                    ans = max(ans, sz)

        return ans