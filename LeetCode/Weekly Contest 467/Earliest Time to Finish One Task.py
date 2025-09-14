from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mini = float('inf')

        for s, t in tasks:
            mini = min(mini, s + t)

        return mini