from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        original = 0
        for i in range(n):
            original += strategy[i] * prices[i]


        ans = original

        slide = 0
        for i in range(k):
            original -= prices[i] * strategy[i]

        for i in range(k // 2, k):
            slide += prices[i]

        ans = max(ans, original + slide)

        for i in range(k, n):
            slide += prices[i]
            slide -= prices[i - k//2]
            original += prices[i - k] * strategy[i - k]
            original -= prices[i] * strategy[i]
            ans = max(ans, slide + original)

        return ans