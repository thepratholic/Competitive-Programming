class Solution:
    def findMaxX(self, n : int) -> int:
        # code here
        i = 1
        while True:
            if (2 ** i) > n:
                return i - 1
            else:
                i += 1

        return -1