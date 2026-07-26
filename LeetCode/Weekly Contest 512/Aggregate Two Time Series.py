class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i = j = 0
        n = len(series1)
        m = len(series2)

        ans = []

        while i < n or j < m:
            if j == m or (i < n and series1[i][0] < series2[j][0]):
                t = series1[i][0]

                v1 = series1[i][1]
                v2 = series2[j][1] if j < m else 0

                ans.append([t, v1 + v2])
                i += 1

            elif i == n or series2[j][0] < series1[i][0]:
                t = series2[j][0]

                v1 = series2[j][1]
                v2 = series1[i][1] if i < n else 0

                ans.append([t, v1 + v2])
                j += 1
            else:
                t = series1[i][0]
                ans.append([t, series1[i][1] + series2[j][1]])
                i += 1
                j += 1

        return ans