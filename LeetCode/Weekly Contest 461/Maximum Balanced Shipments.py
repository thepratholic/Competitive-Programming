from typing import List


class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        stack = []

        ans = 0
        for i in range(n):
            if i == 0 or not stack:
                stack.append(weight[i])

            else:
                if stack and weight[i] < stack[-1]:
                    ans += 1
                    stack.clear()

                else:
                    stack.append(weight[i])

        return ans