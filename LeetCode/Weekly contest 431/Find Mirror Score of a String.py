class Solution:
    def calculateScore(self, s: str) -> int:
        n = len(s)

        occ = [[] for _ in range(26)]
        ans = 0

        for i in range(n):
            mirror = chr(ord('a') + ord('z') - ord(s[i]))

            if occ[ord(mirror) - ord('a')]:
                ans += i - occ[ord(mirror) - ord('a')][-1]
                occ[ord(mirror) - ord('a')].pop()
            else:
                occ[ord(s[i]) - ord('a')].append(i)

        return ans