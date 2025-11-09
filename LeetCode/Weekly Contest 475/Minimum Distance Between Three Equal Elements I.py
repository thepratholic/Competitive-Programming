from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if (i != j and j != k and k != i) and (nums[i] == nums[j] == nums[k]):
                        ans = min(ans, abs(i - j) + abs(j - k) + abs(k - i))

        return ans if ans != float('inf') else -1