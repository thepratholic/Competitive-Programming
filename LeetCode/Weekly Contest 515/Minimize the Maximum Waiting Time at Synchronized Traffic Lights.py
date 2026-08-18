class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        arrivalTime.sort()

        ans = 0

        mx = max(lights)

        for a in arrivalTime:
            cur = a % period

            if cur < mx:
                pass

            else:
                ans = max(ans, period - cur)

        return ans