class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)

        ans = s

        for i in range(1, n + 1):
            first = s[ : i][::-1]
            first += s[i:]
        
            if ans > first:
                ans = first


            second = s[:-i] + s[-i : ][::-1]
            if ans > second:
                ans = second

        return ans