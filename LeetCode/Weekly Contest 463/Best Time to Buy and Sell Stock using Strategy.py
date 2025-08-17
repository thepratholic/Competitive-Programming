from typing import List


class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2

        original = 0
        for i in range(n):
            original += strategy[i] * prices[i]


        prefix_old = [0] * (n + 1) 
        prefix_price = [0] * (n + 1)   
        for i in range(n):
            prefix_old[i + 1] = prefix_old[i] + strategy[i] * prices[i]
            prefix_price[i + 1] = prefix_price[i] + prices[i]

        best = original

        for start in range(n - k + 1):
            end = start + k
            old_sum = prefix_old[end] - prefix_old[start]
            new_sum = prefix_price[end] - prefix_price[start + half]
            cand = original - old_sum + new_sum
            if cand > best:
                best = cand

        return best