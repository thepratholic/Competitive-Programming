class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n = len(nums)

        options = [dict() for _ in range(n)]

        for i, x in enumerate(nums):
            cur = x
            div_cost = 0

            while True:
                val = cur
                mul_cost = 0

                while val <= 2 * sum:
                    cost = div_cost + mul_cost

                    if val <= sum:
                        if val not in options[i]:
                            options[i][val] = cost

                        else:
                            options[i][val] = min(options[i][val], cost)

                    if val == 0:
                        break

                    val *= 2
                    mul_cost += 1

                if cur == 0:
                    break

                cur //= 2
                div_cost += 1

        INF = 10 ** 30
        dp = [[INF] * (sum + 1) for _ in range(n + 1)]

        for idx in range(n + 1):
            dp[idx][0] = 0

        for idx in range(n - 1, -1, -1):
            for rem in range(1, sum + 1):

                dp[idx][rem] = dp[idx + 1][rem]

                for val, cost in options[idx].items():
                    if val <= rem:
                        dp[idx][rem] = min(dp[idx][rem], cost + dp[idx + 1][rem - val])

        ans = dp[0][sum]

        return ans if ans != INF else -1