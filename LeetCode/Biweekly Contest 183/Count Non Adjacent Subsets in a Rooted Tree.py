from functools import cache
from typing import List


class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        MOD = (10 ** 9) + 7

        n = len(parent)

        tree = [[] for _ in range(n)]

        for node in range(1, n):
            par = parent[node]
            tree[par].append(node)

        @cache
        def dfs(node, take):

            dp = [0] * k

            if take:
                rem = nums[node] % k
                dp[rem] = 1

            else:
                dp[0] = 1

            for child in tree[node]:

                if take:
                    child_dp = dfs(child, 0)

                else:
                    not_take = dfs(child, 0)
                    take_child = dfs(child, 1)

                    child_dp = [0] * k

                    for r in range(k):
                        child_dp[r] = (not_take[r] + take_child[r]) % MOD
                        
                    
                new_dp = [0] * k # child se bhi result aagya, and current node tak ka bhi hai, so dono ko merge karke upar bhej do parent side pe

                for r1 in range(k):

                    if dp[r1] == 0: continue

                    for r2 in range(k):

                        if child_dp[r2] == 0: continue

                        new_rem = (r1 + r2) % k

                        new_dp[new_rem] += (dp[r1] * child_dp[r2])
                        new_dp[new_rem] %= MOD

                dp = new_dp

            return tuple(dp)

        ans = (dfs(0, 0)[0] + dfs(0, 1)[0]) % MOD

        ans = (ans - 1 + MOD) % MOD

        return ans