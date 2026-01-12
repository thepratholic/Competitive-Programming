from typing import List


class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(n):
            s = 0
            st = set()

            for r in range(l, n):
                s += nums[r]
                st.add(nums[r])
                if s in st:
                    ans += 1

        return ans