from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)

        prev = [0] * n

        for j in range(m):
            for i in range(n):
                if i == 0:
                    prev[i] = prev[i] + skill[i] * mana[j]
                else:
                    prev[i] = max(prev[i], prev[i - 1]) + skill[i] * mana[j]

            for i in range(n - 2, -1, -1):
                prev[i] = prev[i + 1] - skill[i + 1] * mana[j]

        return prev[n - 1]