class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        peak = 0
        valley = 0

        for x in range(num1, num2 + 1):
            s = str(x)
            
            if len(s) < 3:
                continue

            for i in range(1, len(s) - 1):
                if int(s[i]) > int(s[i - 1]) and int(s[i]) > int(s[i + 1]):
                    # peak
                    peak += 1
                elif int(s[i]) < int(s[i - 1]) and int(s[i]) < int(s[i + 1]):
                    # valley
                    valley += 1

        return peak + valley