from typing import Counter


class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        n = len(s)

        freq = Counter(t)

        ans = []

        for i in range(n):
            s_bit = s[i]
            need = '1' if s_bit == '0' else '0'

            if freq.get(need, 0) > 0:
                ans.append('1')
                freq[need] -= 1
                if freq[need] == 0:
                    del freq[need]

            else:
                ans.append('0')
                freq[s_bit] -= 1
                if freq[s_bit] == 0:
                    del freq[s_bit]

        return "".join(ans)