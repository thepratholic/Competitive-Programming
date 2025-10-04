class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        seen = {(0, 0)}
        x = y = 0
        for i in range(k, len(s)):
            if s[i] == 'U': y += 1
            if s[i] == 'D': y -= 1
            if s[i] == 'L': x -= 1
            if s[i] == 'R': x += 1

            if s[i - k] == 'U': y -= 1
            if s[i - k] == 'D': y += 1
            if s[i - k] == 'L': x += 1
            if s[i - k] == 'R': x -= 1

            seen.add((x, y))
        return len(seen)
