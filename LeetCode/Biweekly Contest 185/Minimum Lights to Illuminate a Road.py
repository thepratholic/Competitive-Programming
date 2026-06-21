class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        diff = [0] * (n + 1)
        for i, v in enumerate(lights):
            if v > 0:
                l = max(0, i - v)
                r = min(n - 1, i + v)

                diff[l] += 1
                diff[r + 1] -= 1


        cover = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur > 0:
                cover[i] = True

        ans = 0
        i = 0

        while i < n:
            if not cover[i]:
                j = i

                while j < n and not cover[j]:
                    j += 1

                sz = j - i

                ans += (sz + 2) // 3
                i = j

            else:
                i += 1

        return ans