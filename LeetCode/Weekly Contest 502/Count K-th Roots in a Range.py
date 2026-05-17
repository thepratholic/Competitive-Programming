class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:

        if k == 1:
            return r - l + 1

        ans = 0

        for i in range(int(1e5)):
            num = pow(i, k)

            if num > r: break # prune

            if num >= l and num <= r:
                ans += 1

        return ans