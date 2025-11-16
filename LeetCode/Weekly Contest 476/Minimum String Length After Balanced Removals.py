from typing import Counter


class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        n = len(s)

        freq = Counter(s)

        a_freq = freq['a']
        b_freq = freq['b']

        return abs(a_freq - b_freq)
        