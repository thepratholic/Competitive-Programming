class Solution:
    def isPossible(self, s : str) -> bool:
        # code here
        n = len(s)

        total_wins = 0

        rem = 14 - n

        for i in range(n):
            if s[i] == "W":
                total_wins += 1

        if rem + total_wins >= 8:
            return True

        else:
            return False