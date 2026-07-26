class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0

        if s > 9 * n:
            return -1

        ans = []
        for _ in range(n):
            d = min(9, s)
            ans.append(str(d))
            s -= d

        return int("".join(ans).lstrip("0")) or int("0")