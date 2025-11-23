from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7
        m = len(s)

        pref_sum = [0] * (m + 1) # for sum for non-0 digits
        pref_cnt = [0] * (m + 1) # non zero digits ka count i tak
        pref_val = [0] * (m + 1) # kitna ans vo bana rha hai, i tak, i.e 'x' bana rha
        pow10 = [1] * (m + 1)

        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        for i in range(1, m + 1):
            d = int(s[i - 1])
            pref_sum[i] = pref_sum[i - 1]
            pref_cnt[i] = pref_cnt[i - 1]
            pref_val[i] = pref_val[i - 1]

            if d != 0:
                pref_sum[i] += d
                pref_cnt[i] += 1
                pref_val[i] = (pref_val[i - 1] * 10 + d) % MOD

        ans = []
        for l, r in queries:
            l += 1
            r += 1

            total_sum = pref_sum[r] - pref_sum[l - 1]

            if total_sum == 0: 
                ans.append(0)
                continue

            cnt = pref_cnt[r] - pref_cnt[l - 1]

            x = (pref_val[r] - (pref_val[l - 1] * pow10[cnt] % MOD) + MOD) % MOD

            ans.append((x * total_sum) % MOD)

        return ans