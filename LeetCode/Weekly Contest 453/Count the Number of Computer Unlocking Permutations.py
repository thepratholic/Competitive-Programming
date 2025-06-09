from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        M = 10**9 + 7
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        for i in range(1, n):
            ans = (ans * i) % M

        return ans % M