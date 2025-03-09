from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        unplaced = 0
        
        
        available_baskets = [True] * n 
        
        for i in range(n):
            fruit_quantity = fruits[i]
            placed = False
            
            for j in range(n):
                if available_baskets[j] and baskets[j] >= fruit_quantity:
                    available_baskets[j] = False 
                    placed = True
                    break
                    
            if not placed:
                unplaced += 1
                
        return unplaced
