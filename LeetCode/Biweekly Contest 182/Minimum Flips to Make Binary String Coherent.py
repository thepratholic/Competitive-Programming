class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')

        all_z = ones
        all_o = n - ones

        one_1 = max(0, ones - 1) # ones and k is same here

        start = 1 if s[0] == '0' else 0
        end = 1 if s[-1] == '0' else 0

        mid = max(0, ones - (1 if s[0] == '1' else 0) - (1 if s[-1] == '1' else 0))

        b = mid + start + end

        return min(b, all_z, all_o, one_1)