from typing import List


class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        n = len(words)

        ans = 0

        vis = {}
        for i in range(n):
            word = words[i]
            if len(word) >= k:
                vis[word[:k]] = vis.get(word[:k], 0) + 1

        for cnt in vis.values():
            if cnt >= 2:
                ans += 1

        return ans