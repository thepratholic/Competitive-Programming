from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_factor = max(f for f, _ in items)
        min_cost = min(p for _, p in items)

        freq = [0] * (max_factor + 1)
        for f, p in items:
            freq[f] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] == 0: 
                continue

            total = 0
            for m in range(f, max_factor + 1, f):
                total += freq[m]

            multiples[f] = total

        valid_moves = []
        for f, p in items:
            limit = multiples[f] - 1

            if limit > 0 and p < 2 * min_cost:
                valid_moves.append((p, limit))

        valid_moves.sort()
        ans = 0

        for price, limit in valid_moves:
            take = min(limit, budget // price)
            ans += 2 * take
            budget -= (take * price)

        ans += budget // min_cost
        return ans