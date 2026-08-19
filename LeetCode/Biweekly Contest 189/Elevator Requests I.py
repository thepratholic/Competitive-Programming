class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        ans = 0

        ans += abs(requests[0] - 0)
        for i in range(1, len(requests)):
            ans += abs(requests[i] - requests[i - 1])

        return ans