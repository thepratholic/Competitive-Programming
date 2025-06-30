from typing import List


class Solution:
    def find_lcp(self, words, x, y):
        n = min(len(words[x]), len(words[y]))
        count = 0
        for j in range(n):
            if words[x][j] != words[y][j]: break
            count += 1

        return count

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        if n <= 2:
            return [0] * n

        lcps = []
        for i in range(1, n):
            lcps.append(self.find_lcp(words, i - 1, i))

        pre, suff = [0] * n, [0] * n

        for i in range(1, n):
            pre[i] = max(pre[i - 1], lcps[i - 1])

        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], lcps[i])

        ans = [0] * n
        ans[0] = suff[1]

        for i in range(1, n - 1):
            ans[i] = max((pre[i - 1], suff[i + 1], self.find_lcp(words, i - 1, i + 1)))

        ans[n - 1] = pre[n - 2]
        return ans