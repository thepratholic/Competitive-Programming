from typing import List


class Solution:
    def maxPoints(self, tech1: List[int], tech2: List[int], k: int) -> int:
        n = len(tech1)
        ans = 0

        taken = set()

        diffs = []
        for i in range(n):
            diffs.append((tech1[i] - tech2[i], i))

        diffs.sort(reverse = True)

        for d, i in diffs[:k]:
            ans += tech1[i]
            taken.add(i)

        for d, i in diffs[k:]:
            ans += max(tech1[i], tech2[i])

        return ans