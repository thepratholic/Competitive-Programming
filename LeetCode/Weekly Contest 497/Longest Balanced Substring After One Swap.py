class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        def f(st):
            total_1 = st.count('1')
            total_0 = n - total_1

            pre = 0
            mp = {}
            mp[pre] = -1
            ans = 0

            cnt_1 = total_1
            cnt_0 = total_0

            for i in range(n):
                if st[i] == '1':
                    pre += 1
                    cnt_1 -= 1

                else:
                    pre -= 1
                    cnt_0 -= 1

                if pre in mp:
                    ans = max(ans, i - mp[pre])

                if (pre + 2) in mp and cnt_1 > 0:
                    ans = max(ans, i - mp[pre + 2])

                if (pre - 2) in mp and cnt_0 > 0:
                    ans = max(ans, i - mp[pre - 2])

                if pre not in mp:
                    mp[pre] = i

            return ans

        return max(f(s), f(s[::-1]))