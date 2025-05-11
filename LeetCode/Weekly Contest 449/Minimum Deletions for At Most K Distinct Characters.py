from typing import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        mpp = Counter(s)
        n = len(s)

        ans = 0
        if len(mpp) == k:
            return ans

        freq_list = sorted(mpp.items(), key=lambda x: x[1])

        while len(mpp) > k:
            ch, freq = freq_list.pop(0)
            ans += freq
            del mpp[ch]

        return ans