from typing import DefaultDict


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        n = len(s)

        normal = "abcdefghijklmnopqrstuvwxyz"
        mirror = normal[::-1]

        mpp = {}
        for i in range(len(normal)):
            mpp[normal[i]] = mirror[i]

        for i in range(10):
            mpp[str(i)] = str(9 - i)

        freq = DefaultDict(int)
        vis = set()
        ans = 0
        for c in s:
            freq[c] += 1


        for c in freq:
            if c not in vis:
                m = mpp[c]

                ans += abs(freq[c] - freq.get(m, 0))
                vis.add(m)
                vis.add(c)

        return ans