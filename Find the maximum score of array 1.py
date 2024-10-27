from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        def lcm(a: int, b: int) -> int:
            return (a * b) // gcd(a, b)

        def array_gcd(arr: List[int]) -> int:
            if not arr:
                return 0
            result = arr[0]
            for i in range(1, len(arr)):
                result = gcd(result, arr[i])
            return result

        def array_lcm(arr: List[int]) -> int:
            if not arr:
                return 0
            result = arr[0]
            for i in range(1, len(arr)):
                result = lcm(result, arr[i])
            return result

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0] * nums[0]

        max_score = 0

        for i in range(n):

            temp_arr = nums[:i] + nums[i+1:]
            current_gcd = array_gcd(temp_arr)
            current_lcm = array_lcm(temp_arr)
            max_score = max(max_score, current_gcd * current_lcm)

        original_gcd = array_gcd(nums)
        original_lcm = array_lcm(nums)
        max_score = max(max_score, original_gcd * original_lcm)
        return max_score