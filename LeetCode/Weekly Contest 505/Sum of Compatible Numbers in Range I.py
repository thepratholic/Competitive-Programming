class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:

        ans = 0

        for i in range(1, 200):
            if abs(n - i) <= k and (n & i) == 0:
                ans += i

        return ans