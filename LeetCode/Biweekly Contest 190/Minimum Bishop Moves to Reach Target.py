class Solution:
    def minBishopMoves(self, s: list[int], t: list[int]) -> int:

        sr, sc = s
        tr, tc = t

        if abs(sr - tr) == abs(sc - tc):
            return 1

        if (sr + sc) % 2 == (tr + tc) % 2:
            return 2

        return -1