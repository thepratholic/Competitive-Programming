class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)

        if n == 1:
            if s1[0] == '1' and s2[0] == '0':
                return -1

            elif s1 == s2:
                return 0

            return 1 

        ans = 0
        i = 0

        while i < n:
            if s1[i] == '0' and s2[i] == '1':
                ans += 1
                i += 1

            elif s1[i] == '1' and s2[i] == '0':
                j = i

                while j < n and s1[j] == '1' and s2[j] == '0':
                    j += 1

                sz = j - i
                ans += (sz // 2)

                if sz & 1:
                    ans += 2 # aage bhi ek chahiye hoga to pair single wala

                i = j

            else:
                i += 1

        return ans