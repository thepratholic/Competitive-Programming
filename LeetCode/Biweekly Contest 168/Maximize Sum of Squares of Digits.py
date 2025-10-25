class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num == 1 and sum <= 9:
            return str(sum)
        elif num == 1 and sum > 9:
            return ""


        ans = []
        for i in range(num):
            d = min(9, sum)

            ans.append(str(d))
            sum -= d

        if sum != 0:
            return ""

        return "".join(ans)