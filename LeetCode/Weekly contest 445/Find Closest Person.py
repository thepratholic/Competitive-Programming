class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first_to_third = abs(z - x)
        second_to_third = abs(z - y)

        if first_to_third == second_to_third:
            return 0

        elif first_to_third > second_to_third:
            return 2

        else:
            return 1