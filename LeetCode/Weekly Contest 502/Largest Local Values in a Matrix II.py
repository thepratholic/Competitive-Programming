from typing import List


class Solution:
    def countLocalMaximums(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        pos = [[] for _ in range(201)]

        for i in range(n):
            for j in range(m):
                pos[matrix[i][j]].append((i, j))

        ans = 0

        for r in range(n):
            for c in range(m):
                x = matrix[r][c]

                if x == 0:
                    continue

                ok = True # assuming yeh local mx ban jayega

                r1 = r - x
                r2 = r + x
                c1 = c - x
                c2 = c + x

                for val in range(x + 1, 201):
                    for i, j in pos[val]:

                        if i >= r1 and i <= r2 and j >= c1 and j <= c2:

                            dr = abs(i - r)
                            dc = abs(j - c)
    
                            if dr == x and dc == x:
                                continue
    
                            ok = False
                            break

                    if not ok:
                        break

                if ok:
                    ans += 1

        return ans