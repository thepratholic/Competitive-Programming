from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        cnt = 0

        for i in range(n):
            placed =  False

            for j in range(n):
                if baskets[j] >= fruits[i]:
                    baskets[j] = 0
                    placed = True
                    break

            if placed is False:
                cnt += 1


        return cnt
