from typing import List


class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        target = tuple(target)

        seen = set(map(tuple, points))

        if target in seen:
            return 0 # pehle se hi hai

        if len(seen) < 2:
            return -1

        g = 0

        while True:

            arr = list(seen)

            new = set()

            m = len(arr)

            for i in range(m):
                x, y, z = arr[i]

                for j in range(i + 1, m):

                    x2, y2, z2 = arr[j]

                    c = ((x + x2) // 2, (y + y2) // 2, (z + z2) // 2)

                    if c not in seen:
                        new.add(c)

            if not new:
                return -1

            g += 1

            if target in new:
                return g

            seen |= new