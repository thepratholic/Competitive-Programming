from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        pizzas.sort()

        total_days = n // 4

        cur = n - 1
        total_weight = 0
        for day in range(1, total_days + 1, 2):
            total_weight += pizzas[cur]
            cur -= 1

        cur -= 1

        for day in range(2, total_days + 1, 2):
            total_weight += pizzas[cur]
            cur -= 2

        return total_weight