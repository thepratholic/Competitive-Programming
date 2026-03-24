class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and ((nums[stack[-1]] | nums[i]) > nums[stack[-1]]):
                idx = stack.pop()
                right[idx] = i # means vo nums[idx] wala element ka right boundary yahi hai
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and ((nums[stack[-1]] | nums[i]) > nums[stack[-1]] or nums[i] == nums[stack[-1]]):
                idx = stack.pop()
                left[idx] = i

            stack.append(i)

        ans = 0
        for i in range(n):
            l = i - left[i]
            r = right[i] - i
            ans += (l * r)

        return ans