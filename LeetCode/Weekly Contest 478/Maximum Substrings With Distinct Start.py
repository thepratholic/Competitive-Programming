class Solution:
    def maxDistinct(self, s: str) -> int:
        n = len(s)

        cnt = [0] * 26

        for ch in s:
            val = ord(ch) - ord('a')

            if cnt[val] != 0: continue
            else:
                cnt[val] = 1

        return sum(cnt)