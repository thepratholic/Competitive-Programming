from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, words: List[str]) -> int:
        n = len(words)
        freq = defaultdict(int)

        ans = 0
        for word in words:
            b = ord(word[0]) - ord('a')
            k = []

            for ch in word:
                k.append((ord(ch) - ord('a') - b) % 26)

            freq[tuple(k)] += 1

        for cnt in freq.values():
            ans += (cnt * (cnt - 1) // 2)
        return ans