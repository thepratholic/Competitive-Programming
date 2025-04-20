from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)

        i = 0
        vis = [False] * n

        score = 0

        while 0 <= i < n and not vis[i]:
            vis[i] = True
            if instructions[i] == "add":
                score += values[i]
                i += 1

            elif instructions[i] == "jump":
                i += values[i]

        return score