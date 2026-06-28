from typing import List


class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:
        intervals = sorted(occupiedIntervals)

        merge = []

        for start, end in intervals:
            if merge and start <= merge[-1][1] + 1:
                merge[-1][1] = max(merge[-1][1], end)

            else:
                merge.append([start, end])

        res = []

        for s, e in merge:
            if freeEnd < s or freeStart > e:
                res.append([s, e])

            elif freeStart <= s and freeEnd >= e:
                pass

            elif freeStart <= s and freeEnd < e:
                res.append([freeEnd + 1, e])

            elif freeStart > s and freeEnd >= e:
                res.append([s, freeStart - 1])

            else:
                res.append([s, freeStart - 1])
                res.append([freeEnd + 1, e])

        return res