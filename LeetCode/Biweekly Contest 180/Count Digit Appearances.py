class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        n = len(nums)

        ans = 0

        def check(number):
            cnt = 0
            while number > 0:
                ld = number % 10
                if ld == digit:
                    cnt += 1

                number //= 10

            return cnt

        for num in nums:
            ans += check(num)

        return ans