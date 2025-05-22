from typing import List


class Solution:
    def getSum(self, n):
        res = 0
        while n:
            res += (n % 10)
            n //= 10
        return res

    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        digitPair = []

        for i in range(n):
            sum_of_digit = self.getSum(nums[i])
            digitPair.append((sum_of_digit, nums[i], i))

        digitPair.sort(key = lambda x : (x[0], x[1]))

        position = [0] * n
        for sorted_idx in range(n):
            original_index = digitPair[sorted_idx][2]
            position[original_index] = sorted_idx

        vis = [False] * n
        swaps = 0
        for i in range(n):
            if vis[i] or position[i] == i:
                continue

            cycles = 0
            j = i
            while not vis[j]:
                vis[j] = True
                j = position[j]
                cycles += 1

            swaps += (cycles - 1)
        return swaps