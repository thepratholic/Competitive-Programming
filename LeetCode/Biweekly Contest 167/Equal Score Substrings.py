class Solution:
    def scoreBalance(self, s: str) -> bool:
        n = len(s)

        total = 0
        for ch in s:
            total += (ord(ch) - ord('a') + 1)

        if total & 1:
            return False

        ans = 0
        for ch in s:
            ans += (ord(ch) - ord('a') + 1)
            if ans == total // 2:
                return True

        return False