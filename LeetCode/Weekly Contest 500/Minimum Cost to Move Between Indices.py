class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        closest = [0] * n

        for i in range(n):
            if i == 0:
                closest[i] = 1

            elif i == n - 1:
                closest[i] = n - 2

            else:
                left = nums[i] - nums[i - 1]
                right = nums[i + 1] - nums[i]

                if left <= right:
                    closest[i] = i - 1

                else:
                    closest[i] = i + 1

        pref = [0] * n
        for i in range(n - 1):
            cost = 1 if closest[i] == i + 1 else nums[i + 1] - nums[i]
            pref[i + 1] = pref[i] + cost

        suf = [0] * n
        for i in range(n - 1, 0, -1):
            cost = 1 if closest[i] == i - 1 else nums[i] - nums[i - 1]
            suf[i - 1] = suf[i] + cost

        ans = []
        for l, r in queries:
            if l < r:
                ans.append(pref[r] - pref[l])


            else:
                ans.append(suf[r] - suf[l])


        return ans