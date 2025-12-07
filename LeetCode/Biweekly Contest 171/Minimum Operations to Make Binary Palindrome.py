from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            cur = nums[i]

            b_cur = bin(cur)[2:]

            if b_cur == b_cur[::-1]:
                continue

            else:
                # we have to make binary
                res1 = 0
                t1 = cur
                while bin(t1)[2:] != bin(t1)[2:][::-1]:
                    t1 -= 1
                    res1 += 1

                t2 = cur
                res2 = 0
                while bin(t2)[2:] != bin(t2)[2:][::-1]:
                    t2 += 1
                    res2 += 1

                ans[i] = min(res1, res2)

        return ans
            