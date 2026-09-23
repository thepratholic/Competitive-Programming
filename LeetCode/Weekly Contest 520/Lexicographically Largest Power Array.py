class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        groups = [nums]
        ans = []

        for i in range(15):
            bit = 14 - i
            power = 0

            j = 0
            while j < len(groups):
                group = groups[j]

                g1 = []
                g0 = []

                for x in group:
                    if x & (1 << bit):
                        g1.append(x)

                    else:
                        g0.append(x)

                power += len(g1)
                if not g0:
                    # saare numbers mein current bit 1 hai
                    j += 1
                    continue

                if not g1:
                    # saare numbers mein cur bit 0 hai
                    break

                groups[j : j + 1] = [g1, g0] # pehle 1's wala group rearrange karke daal dia, so that max prefix rahe

                j += 1

            ans.append(power)

        return ans