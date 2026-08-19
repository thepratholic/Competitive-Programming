from bisect import bisect_left


class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        a = sorted(requests)
        m = len(a)

        INF = 10 ** 30

        k = bisect_left(a, start)

        dp = {}

        for i in (k - 1, k):
            if 0 <= i < m:
                cost = abs(start - a[i]) * m

                dp[(i, i, 0)] = cost
                dp[(i, i, 1)] = cost

        for length in range(1, m):
            rem = m - length
            new_dp = {}

            for (l, r, side), cost in dp.items():
                pos = a[l] if side == 0 else a[r]

                if l > 0:
                    new_cost = cost + abs(pos - a[l - 1]) * rem
                    key = (l - 1, r, 0)

                    new_dp[key] = min(new_dp.get(key, INF), new_cost)

                if r + 1 < m:
                    new_cost = cost + abs(a[r + 1] - pos) * rem
                    key = (l, r + 1, 1)

                    new_dp[key] = min(new_dp.get(key, INF), new_cost)

            dp = new_dp

        return min(cost for (l, r, side), cost in dp.items() if l == 0 and r == m - 1)