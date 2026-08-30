class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        ans = []

        MAX = 1 << 25

        for x in nums:
            cur = []

            while x >= MAX:
                cur.append('z')
                x -= MAX

            while x > 0:
                p = x.bit_length() - 1

                cur.append(chr(ord('a') + p))

                x -= (1 << p)

            ans.append("".join(cur))

        return ans