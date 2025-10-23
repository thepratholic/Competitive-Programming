from bisect import bisect_right

from sortedcontainers import SortedList


class Solution:
    def lexGreaterPermutation(self, s: str, t: str) -> str:
        n = len(s)

        chs = SortedList(s)
        pref = ""
        ans = []

        for i in range(n):

            idx = bisect_right(chs, t[i])

            if idx < len(chs):
                ch = chs[idx]
                tmp = pref + ch + "".join(chs[ : idx] + chs[idx + 1 : ])
                ans.append(tmp)

            if t[i] not in chs:
                break

            pref += t[i]
            chs.remove(t[i])

        if not ans:
            return ""

        return min(ans)