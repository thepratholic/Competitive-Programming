from typing import List


class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        n = len(s)
        ones = s.count('1')

        ans = []

        s_pos = []
        for i, ch in enumerate(s):
            if ch == '1':
                s_pos.append(i)

        for t in strs:
            fixed = t.count('1')
            q = t.count('?')

            need = ones - fixed

            if need < 0 or need > q:
                ans.append(False)
                continue

            arr = list(t)

            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == '?':
                    if need:
                        arr[i] = '1'
                        need -= 1

                    else:
                        arr[i] = '0'

            t_pos = []
            for i, ch in enumerate(arr):
                if ch == '1':
                    t_pos.append(i)

            ok = True
            for a, b in zip(s_pos, t_pos):
                if b < a:
                    ok = False
                    break

            ans.append(ok)

        return ans   