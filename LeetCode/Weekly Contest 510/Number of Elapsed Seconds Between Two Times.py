class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        def f(t):
            h, m, s = map(int, t.split(":"))

            return h * 3600 + m * 60 + s

        return f(endTime) - f(startTime)