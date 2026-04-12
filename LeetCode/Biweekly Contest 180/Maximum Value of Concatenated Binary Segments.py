from functools import cmp_to_key


class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        MOD = (10 ** 9) + 7

        segs = ['1' * a + '0' * b for a, b in zip(nums1, nums0)]

        # i was actually forogot this cmp to key wala function...
        segs.sort(key = cmp_to_key(lambda a, b : (1 if a + b > b + a else -1 if a + b < b + a else 0)), reverse = True)


        res = 0
        for sg in segs:
            for bit in sg:
                res = (res * 2 + int(bit)) % MOD

        return res