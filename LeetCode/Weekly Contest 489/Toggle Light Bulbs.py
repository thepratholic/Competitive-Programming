class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        n = len(bulbs)

        vis = set()

        for i in range(n):
            if bulbs[i] in vis:
                vis.discard(bulbs[i])

            else:
                vis.add(bulbs[i])

        return sorted(list(vis))