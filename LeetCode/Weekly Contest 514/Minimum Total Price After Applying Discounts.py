class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse = True)
        discounts.sort(reverse = True)

        m = len(discounts)
        n = len(prices)

        ans = sum(prices)

        for p, d in zip(prices, discounts):
            ans -= p * d / 100

        return ans