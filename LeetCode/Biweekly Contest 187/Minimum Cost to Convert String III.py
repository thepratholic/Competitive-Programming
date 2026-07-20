class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        INF = 10 ** 18

        pre = []
        for (pat, rep), cost in zip(rules, costs):
            stars = pat.count("*")
            pre.append((pat, rep, len(pat), stars + cost))

        dp = [INF] * (n + 1)
        dp[n] = 0 # end pe aagye, so string entire matched

        for i in range(n - 1, -1 , -1):

            if source[i] == target[i]:
                dp[i] = dp[i + 1]

            # ab saare rules try karke dekho
            for pat, rep, sz, cost in pre:

                if i + sz > n:
                    continue

                ok = True
                for j in range(sz):
                    if pat[j] != '*' and pat[j] != source[i + j]:
                        ok = False
                        break

                if not ok:
                    continue

                ok = True
                for j in range(sz):
                    if rep[j] != target[i + j]:
                        ok = False
                        break

                if not ok:
                    continue

                dp[i] = min(dp[i], cost + dp[i + sz])

        return dp[0] if dp[0] != INF else -1