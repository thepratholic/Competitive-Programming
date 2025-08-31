from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []

        n = len(order)

        for i in range(n):
            if order[i] in friends:
                ans.append(order[i])

        return ans