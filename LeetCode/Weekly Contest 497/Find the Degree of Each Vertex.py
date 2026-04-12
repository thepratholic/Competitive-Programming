class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)

        ans = [0] * n

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    ans[i] += 1
                    ans[j] += 1

        for i in range(n):
            ans[i] //= 2

        return ans