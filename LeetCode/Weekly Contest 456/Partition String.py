from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen = set()
        n = len(s)

        segments = []

        l, r = 0, 0

        curr = ""
        while r < n:
            curr += s[r]

            if curr not in seen:
                seen.add(curr)
                segments.append(curr)
                curr = ""
                r += 1

            else:
                r += 1

        return segments