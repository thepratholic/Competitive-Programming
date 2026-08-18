class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[list[int]]) -> int:
        m = len(requests)

        INF = 10 ** 30

        dp = [[INF] * m for _ in range(1 << m)]

        for i in range(m): # start se har ek floor pe sidha
            a, f = requests[i]

            dist = abs(f - start)
            time = max(dist, a)

            dp[1 << i][i] = time

        
        # trying by taking masks
        for mask in range(1 << m):

            for last in range(m):
                if dp[mask][last] == INF:
                    continue

                cur_time = dp[mask][last]
                cur_floor = requests[last][1]

                # dusri requests try karo fulfill karne ka
                for i in range(m):
                    if mask & (1 << i):
                        continue

                    a, nxt = requests[i]

                    travel = abs(cur_floor - nxt)
                    time = max(cur_time + travel, a)

                    new_mask = mask | (1 << i)

                    dp[new_mask][i] = min(dp[new_mask][i], time)


        return min(dp[(1 << m) - 1])