class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        xi = ord(x) - ord('a')
        yi = ord(y) - ord('a')

        ans = []

        ans.extend(y * freq[yi])
        freq[yi] = 0

        ans.extend(x * freq[xi])
        freq[xi] = 0

        for i in range(26):
            if freq[i]:
                ans.extend(chr(i + ord('a')) * freq[i])

        return "".join(ans)