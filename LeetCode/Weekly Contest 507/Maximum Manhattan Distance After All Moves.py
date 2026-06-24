class Solution:
    def maxDistance(self, moves: str) -> int:
        n = len(moves)

        x, y = 0, 0
        other = 0

        for ch in moves:
            if ch == 'L': x -= 1
            elif ch == 'D': y -= 1
            elif ch == 'U': y += 1
            elif ch == 'R': x += 1
            else:
                other += 1

        return abs(0 - x) + abs(0 - y) + other