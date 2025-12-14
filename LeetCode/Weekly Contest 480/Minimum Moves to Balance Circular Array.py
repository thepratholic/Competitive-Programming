from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        pos = 0
        negs = 0
        for num in balance:
            if num > 0:
                pos += num
            else: negs += num

        if pos < abs(negs): return -1

        k = -1
        for i in range(n):
            if balance[i] < 0:
                k = i
                break

        if k == -1: return 0

        need = abs(balance[k])
        cost = 0
        left_d, right_d = 1, 1
        left_i, right_i = (k - 1) % n, (k + 1) % n
        
        while need > 0:
            if left_d <= right_d:
                take = min(balance[left_i], need)
                cost += (take * left_d)
                need -= take
                balance[left_i] -= take
                left_d += 1
                left_i = (left_i - 1) % n

            else:
                take = min(balance[right_i], need)
                cost += (take * right_d)
                need -= take
                balance[right_i] -= take
                right_d += 1
                right_i = (right_i + 1) % n

        return cost