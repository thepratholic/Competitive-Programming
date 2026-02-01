class Solution:
    def countMonobit(self, n: int) -> int:

        ans = 0
        for num in range(n + 1):

            binary = bin(num)[2:]

            if len(set(binary)) == 1:
                ans += 1

        return ans