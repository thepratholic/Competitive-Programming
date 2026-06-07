class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        ans = []

        for mask in range(1 << n):
            cost = 0
            ok = True

            for i in range(n):
                if mask & (1 << i):
                    cost += i

                    if i > 0 and (mask & (1 << (i - 1))):
                        ok = False
                        break

            if ok and cost <= k:
                s = ""

                for i in range(n):
                    if mask & (1 << i):
                        s += "1"

                    else:
                        s += "0"

                ans.append(s)

        return ans
                