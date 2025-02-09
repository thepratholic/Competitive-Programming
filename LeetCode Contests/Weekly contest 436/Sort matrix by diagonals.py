from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        
        def sort_diagonal(row, col, ascending):
            diagonal = []
            i, j = row, col

            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1

            diagonal.sort(reverse=not ascending)

            i, j = row, col
            for val in diagonal:
                grid[i][j] = val
                i += 1
                j += 1

        for j in range(1, n):
            sort_diagonal(0, j, ascending=True)

        for i in range(n):
            sort_diagonal(i, 0, ascending=False)

        return grid©leetcode