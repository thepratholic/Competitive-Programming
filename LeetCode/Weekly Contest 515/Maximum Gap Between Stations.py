class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        m = len(station)

        left = [0] * n
        right = [0] * n

        j = 0
        for i in range(n):
            while station[j] != skill[i]:
                j += 1

            left[i] = j
            j += 1

        j = m - 1
        for i in range(n - 1, -1, -1):
            while station[j] != skill[i]:
                j -= 1

            right[i] = j
            j -= 1

        ans = 0

        for i in range(1, n):
            ans = max(ans, right[i] - left[i - 1])

        return ans