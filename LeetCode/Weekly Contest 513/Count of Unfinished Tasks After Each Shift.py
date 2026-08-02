from bisect import bisect_right
from typing import List


class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        m = len(shifts)

        ans = []
        pref = [0]

        for x in tasks:
            pref.append(pref[-1] + x)

        total = pref[-1]

        progress = 0

        for t in shifts:
            progress += t

            if progress >= total:
                ans.append(0)
                progress = 0

                continue

            done = bisect_right(pref, progress) - 1

            ans.append(n - done)
        return ans