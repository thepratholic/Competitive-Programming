class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        mpp = {(0, 0): -1}

        ans = 1
        v1, v2 = 0, 0

        for i in range(n):

            if s[i] == 'a':
                v1 += 1
                v2 += 1
            elif s[i] == 'c':
                v2 -= 1
            else:
                v1 -= 1

            if (v1, v2) not in mpp:
                mpp[(v1, v2)] = i
            
            ans = max(ans, i - mpp[(v1, v2)])


        comb = ["ab", "ac", "bc"]
        for c in comb:

            x, y = c[0], c[1]

            mpp = {0: -1}
            v = 0
            for i in range(n):
                if s[i] == x:
                    v += 1
                elif s[i] == y:
                    v -= 1
                else:
                    mpp.clear()
                    v = 0
                    mpp[0] = i
                    continue

                if v not in mpp:
                    mpp[v] = i

                ans = max(ans, i - mpp[v])


        cnt = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cnt += 1

            else:
                cnt = 1

            ans = max(ans, cnt)

        return ans 