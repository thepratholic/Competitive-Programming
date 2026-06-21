class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = [['#'] * n for _ in range(m)]

        for col in range(n):
            ans[0][col] = '.'

        for row in range(m):
            ans[row][n - 1] = '.'

        return ["".join(row) for row in ans]