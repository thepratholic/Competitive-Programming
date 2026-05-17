class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = len(s)
        ok = True
        for i in range(1, n):
            if abs(int(s[i - 1]) - int(s[i])) > 2:
                ok = False
                break

        return ok