from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        factors = [f for f, _ in items]
        prices = [p for _, p in items]

        bonus = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and factors[j] % factors[i] == 0:
                    bonus[i] += 1

        dp = [[[0] * 2 for _ in range(budget + 1)] for _ in range(n + 1)]


        for idx in range(n - 1, -1, -1):
            for money in range(budget + 1):
                for taken in range(2):

                    # skip item
                    ans = dp[idx + 1][money][0]

                    if money >= prices[idx]:
                        if taken == 0:
                            ans = max(
                                ans,
                                1 + bonus[idx] + dp[idx][money - prices[idx]][1]
                            )
                        else:
                            ans = max(
                                ans,
                                1 + dp[idx][money - prices[idx]][1]
                            )

                    dp[idx][money][taken] = ans

        return dp[0][budget][0]