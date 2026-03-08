class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        n = len(capacity)
        a = [(x, i) for i, x in enumerate(capacity)]

        a.sort()

        for x, i in a:
            if x >= itemSize:
                return i

        return -1