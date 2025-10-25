from functools import lru_cache
from typing import List


class Solution:
    def countCoprime(self, mat: List[List[int]]) -> int:
        MOD = (10 ** 9) + 7
        m, n = len(mat), len(mat[0])
        
        @lru_cache(None)
        def dfs(row, current_gcd):
            if row == m:
                return 1 if current_gcd == 1 else 0
            
            total = 0
            for num in mat[row]:
                new_gcd = gcd(current_gcd, num)
                total = (total + dfs(row + 1, new_gcd)) % MOD
            return total
        
        return dfs(0, 0)